#!/usr/bin/env python3
"""
基因-疾病分析工作流模板（范本模式）
======================================

本模板可从 SAPHO 替换到任何基因-疾病分析场景。
用法：将此文件复制为新脚本，替换以下4个占位符即可。

替换步骤：
  1. DISEASE_NAME = "你的疾病名称"
  2. GENE_DB     = { "GENE": {...}, ... }  # 替换为你的基因知识库
  3. API查询函数保留，仅调整搜索关键词
  4. 报告模板中的文本替换为你的疾病名

用法:
  python template_workflow.py --list
  python template_workflow.py GENE_NAME
  python template_workflow.py --all
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import requests
except ImportError:
    print("[!] 请先安装依赖: pip install requests")
    sys.exit(1)


# ============================================================================
# [占位符1] 疾病名称 —— 替换为你的目标疾病
# ============================================================================
DISEASE_NAME = "SAPHO综合征"
DISEASE_ABBR = "SAPHO"  # 用于API搜索的关键词

# ============================================================================
# [占位符2] 基因知识库 —— 替换为你的基因列表
# ============================================================================
GENE_DB = {
    "GENE_NAME": {  # <-- 替换
        "gene_name": "GENE_NAME",
        "full_name": "Full Gene Name",
        "locus": "1p13.3",
        "omim_id": "123456",
        "association_strength": "★★★ 中",
        "pathomechanism": "致病机制描述",
        "clinical_evidence": "临床证据",
        "known_variants": [
            {"variant": "p.ExampleVariant", "dbSNP": "rs12345", "significance": "可能致病性", "sources": ["ClinVar", "文献"]},
        ],
        "therapeutic_implications": "治疗靶点提示",
        "disease_forms": ["疾病A", "疾病B"],
    },
}

# 实际SAPHO数据预留 —— 替换上面GENE_DB即可，参考sapho_analysis_pipeline.py

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"


# ============================================================================
# API查询函数（通用，无需修改）
# ============================================================================

def query_api(db: str, gene_name: str) -> list[dict]:
    """通用API查询函数"""
    results = []
    if db == "clinvar":
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "clinvar",
            "term": f"{gene_name}[gene] AND pathogenic",
            "retmax": 10,
            "retmode": "json",
        }
        try:
            r = requests.get(url, params=params, timeout=10)
            data = r.json()
            ids = data.get("esearchresult", {}).get("idlist", [])
            results.append({
                "source": "ClinVar",
                "count": len(ids),
                "ids": ids,
                "url": f"https://www.ncbi.nlm.nih.gov/clinvar?term={gene_name}",
            })
        except Exception as e:
            results.append({"source": "ClinVar", "error": str(e)})

    elif db == "pubmed":
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": f"({gene_name}[Title/Abstract]) AND ({DISEASE_ABBR}[Title/Abstract])",
            "retmax": 10,
            "retmode": "json",
            "sort": "date",
        }
        try:
            r = requests.get(url, params=params, timeout=10)
            data = r.json()
            ids = data.get("esearchresult", {}).get("idlist", [])
            results.append({"source": "PubMed", "count": len(ids), "ids": ids})
        except Exception as e:
            results.append({"source": "PubMed", "error": str(e)})

    return results


def generate_report(gene_name: str) -> str:
    """生成单个基因分析报告"""
    info = GENE_DB.get(gene_name)
    if not info:
        return f"# {gene_name}\n\n未在{DISEASE_NAME}知识库中找到该基因信息。\n"

    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = [
        f"# {DISEASE_NAME} 基因分析报告: {gene_name}",
        f"",
        f"> 生成时间: {now}  |  模板: template_workflow.py",
        f"",
        f"---",
        f"",
        f"## 基本信息",
        f"",
        f"| 字段 | 值 |",
        f"|------|------|",
        f"| 基因全名 | {info['full_name']} |",
        f"| 基因座 | {info['locus']} |",
        f"| OMIM ID | {info['omim_id']} |",
        f"| 关联强度 | {info['association_strength']} |",
        f"| 相关疾病谱 | {'; '.join(info['disease_forms'])} |",
        f"",
        f"## 致病机制",
        f"",
        f"{info['pathomechanism']}",
        f"",
        f"## 已知变异",
        f"",
        f"| 变异 | dbSNP | 致病性判定 | 来源 |",
        f"|------|-------|-----------|------|",
    ]

    for v in info["known_variants"]:
        sources_str = "; ".join(v.get("sources", ["未知"]))
        dbSNP = v.get("dbSNP", "未收录")
        lines.append(f"| {v['variant']} | {dbSNP} | {v['significance']} | {sources_str} |")

    lines.extend([
        f"",
        f"## 治疗靶点提示",
        f"",
        f"{info['therapeutic_implications']}",
        f"",
        f"## 外部数据源查询结果",
        f"",
    ])

    apis = ["clinvar", "pubmed"]
    for api_name in apis:
        res = query_api(api_name, gene_name)
        lines.append(f"- {res[0]['source']}: {json.dumps(res[0], ensure_ascii=False, indent=2)}")

    lines.extend([
        f"",
        f"## 下一步建议",
        f"",
        f"1. 详细阅读PubMed最新文献，了解{gene_name}在{DISEASE_NAME}中的最新发现",
        f"2. 检查测序数据中是否存在上述已知变异",
        f"3. 如发现新变异，提交ClinVar进行致病性评估",
        f"4. 关注Kaggle/天池平台的相关竞赛",
        f"",
        f"---",
        f"",
        f"*本报告由 AI 辅助分析流水线自动生成，仅供科研参考。*",
        f"",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=f"{DISEASE_NAME} 基因分析范本")
    parser.add_argument("gene", nargs="?", help="基因名称")
    parser.add_argument("--list", action="store_true", help="列出所有已知关联基因")
    parser.add_argument("--all", action="store_true", help="分析全部已知基因")
    parser.add_argument("--output", "-o", help="输出目录 (默认: output/)")
    args = parser.parse_args()

    out_dir = Path(args.output) if args.output else OUTPUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.list:
        print(f"\n=== {DISEASE_NAME} 已知关联基因列表 ===\n")
        print(f"{'基因':<12} {'基因座':<12} {'关联强度':<16}")
        print("-" * 40)
        for g, info in GENE_DB.items():
            print(f"{g:<12} {info['locus']:<12} {info['association_strength']:<16}")
        print(f"\n总计 {len(GENE_DB)} 个基因\n")
        return

    if args.all:
        for g in GENE_DB:
            report = generate_report(g)
            out_file = out_dir / f"{g}_report.md"
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"[OK] {g} 报告已生成: {out_file}")
        return

    if not args.gene:
        parser.print_help()
        print(f"\n提示: 使用 --list 查看所有基因，或直接指定基因名进行分析")
        return

    gene = args.gene.upper()
    if gene not in GENE_DB:
        print(f"[!] 基因 '{gene}' 不在已知基因库中")
        print(f"    已知基因: {', '.join(GENE_DB.keys())}")
        sys.exit(1)

    print(f"[*] 开始分析 {DISEASE_NAME} 关联基因: {gene}")
    report = generate_report(gene)
    out_file = out_dir / f"{gene}_report.md"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"[OK] 分析报告已生成: {out_file}")


if __name__ == "__main__":
    main()
# [占位符3] 完成后删除此注释
# [占位符4] 参考 docs/SAPHO_knowledge_base.md 更新知识库
# 更多信息见 docs/WORKFLOW.md
