# SAPHO Gene Analysis Pipeline

> AI驱动的SAPHO综合征基因分析工作流
> 基于亿宝智能(老韩)的医疗AI悬赏课题方向

## 项目概述

SAPHO（滑膜炎-痤疮-脓疱病-骨肥厚-骨炎）是一种罕见的风湿免疫/骨科综合征。本项目提供一套完整的 **AI驱动的基因分析工作流**，用于：

- 搜集和分析SAPHO已知关联基因的变异数据
- 利用公共数据库（ClinVar/OpenTargets/PubMed）进行交叉验证
- 生成结构化分析报告，支撑科研论文、竞赛参赛或基金申请

## 快速开始

```bash
# 1. 安装依赖
pip install requests

# 2. 列出所有已知SAPHO关联基因
python scripts/sapho_analysis_pipeline.py --list

# 3. 分析单个基因
python scripts/sapho_analysis_pipeline.py IL36RN

# 4. 分析全部基因（生成综合报告）
python scripts/sapho_analysis_pipeline.py --all
```

## 项目结构

```
sapho_gene_analysis/
├── README.md                        # 本文件
├── LICENSE                          # MIT License
├── .gitignore                       # Git忽略规则
├── requirements.txt                 # Python依赖
├── docs/
│   ├── SAPHO_knowledge_base.md      # SAPHO综合征知识库
│   └── WORFKLOW.md                  # 完整工作流说明（范本模式）
├── scripts/
│   ├── sapho_analysis_pipeline.py   # 核心：基因AI分析流水线
│   ├── template_workflow.py         # [范本] 通用基因分析工作流模板
│   └── monitor_competitions.py      # [范本] 竞赛/悬赏监控脚本
├── data/                            # 基因数据文件
├── output/                          # 分析报告输出
└── notebooks/
```

## 已知SAPHO关联基因

| 基因 | 基因座 | 关联强度 | OMIM | 主要机制 |
|------|--------|----------|------|----------|
| IL36RN | 2q14.1 | ★★★★★ 强 | 615508 | IL-1通路过度激活 |
| PSTPIP1 | 15q24.3 | ★★★★ 较强 | 606347 | PAPA/SAPHO谱系 |
| LPIN2 | 18p11.31 | ★★★★ 较强 | 608758 | Majeed/SAPHO重叠 |
| NOD2 | 16q12.1 | ★★★ 中 | 605956 | NOD信号通路 |
| IL1RN | 2q14.1 | ★★★ 中 | 605432 | IL-1Ra缺陷 |
| CARD8 | 19q13.33 | ★★ 较弱 | 609051 | 炎症小体调控 |
| NLRC4 | 2p22.3 | ★★ 较弱 | 609971 | NLRC4炎症小体 |
| MEFV | 16p13.3 | ★★ 较弱 | 608107 | IL-1通路修饰 |

## 工作流概览

```
输入(基因名) → 知识库匹配 → 外部数据查询 → AI分析 → 结构化报告
                                 ↓
                          ┌─ ClinVar (变异数据)
                          ├─ OpenTargets (靶点关联)
                          └─ PubMed (最新文献)
```

## 奖赏路径

| 路径 | 预计奖赏 | 难度 | 时间线 |
|------|----------|------|--------|
| Kaggle基因竞赛 | $5k-$100k | ★★★ | 1-6个月 |
| 阿里云天池医疗AI赛 | 5万-50万CNY | ★★★ | 1-3个月 |
| 罕见病科研基金 | 50万-500万CNY | ★★★★★ | 6-12个月 |
| GitHub Sponsors开源赞助 | 持续 | ★★ | 持续 |
| SCI论文奖励 | 1万-20万CNY | ★★★ | 3-12个月 |

## 许可证

MIT License
