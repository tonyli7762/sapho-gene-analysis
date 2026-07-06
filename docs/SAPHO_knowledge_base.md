# SAPHO 综合征知识库
## SAPHO Syndrome Knowledge Base for AI-Driven Gene Analysis

## 一、疾病概述

**SAPHO** 是以下5个临床特征的缩写：
- **S**ynovitis（滑膜炎）
- **A**cne（痤疮）
- **P**ustulosis（脓疱病）
- **H**yperostosis（骨肥厚）
- **O**steitis（骨炎）

| 属性 | 内容 |
|------|------|
| ICD-10 | M89.8 |
| OMIM | 604416 (PAPA综合征相关) |
| 罕见病分类 | 风湿免疫/骨科罕见病 |
| 发病率 | 约1/10,000 |
| 中国罕见病目录 | 已收录 |
| 好发年龄 | 儿童至中年均可发病 |
| 性别倾向 | 女性略多于男性 |

## 二、已知关联基因与变异

### 2.1 核心关联基因

| 基因 | 基因座 | 关联强度 | OMIM | 致病机制 | 文献支持 |
|------|--------|----------|------|----------|----------|
| **IL36RN** | 2q14.1 | ★★★★★ 强 | 615508 | IL-36受体拮抗剂缺陷，IL-1通路过度激活 | 多个中国SAPHO队列研究证实 |
| **PSTPIP1** | 15q24.3 | ★★★★ 较强 | 606347 | CD2结合蛋白1突变致PAPA综合征与SAPHO重叠 | PAPA/SAPHO谱系疾病 |
| **LPIN2** | 18p11.31 | ★★★★ 较强 | 608758 | 脂素-2缺陷致Majeed综合征与SAPHO表型重叠 | 儿童SAPHO/CRMO相关 |
| **NOD2** | 16q12.1 | ★★★ 中 | 605956 | Blau综合征相关基因，NOD信号通路调控 | 部分SAPHO患者携带 |
| **IL1RN** | 2q14.1 | ★★★ 中 | 605432 | IL-1受体拮抗剂，与IL36RN通路协同 | 治疗靶点相关 |
| **CARD8** | 19q13.33 | ★★ 较弱 | 609051 | 炎症小体调控蛋白 | 少数病例报告 |
| **NLRC4** | 2p22.3 | ★★ 较弱 | 609971 | NLRC4炎症小体过度激活 | 与SAPHO样表型关联 |
| **MEFV** | 16p13.3 | ★★ 较弱 | 608107 | 家族性地中海热基因，IL-1通路 | 可能修饰SAPHO表型 |

### 2.2 已报道的中国SAPHO队列基因发现

| 研究 | 队列规模 | 关键发现 |
|------|----------|----------|
| 北京协和医院 2021 | 20例 | 2例IL36RN p.Leu27Pro突变 |
| 上海交大瑞金医院 2022 | 35例 | IL36RN突变率约15%，PSTPIP1约8% |
| 华西医院 2023 | 28例 | 发现新的IL36RN剪接位点突变 |
| 广州中山三院 2023 | 42例 | LPIN2 p.Ser734Leu与早发型相关 |

## 三、疾病通路与生物学网络

### 3.1 核心通路
IL-1β 信号通路 —— 核心致病通路
NLRP3 炎症小体 ← IL36RN缺陷(失去抑制)
Caspase-1 → IL-1β成熟
PSTPIP1 过度磷酸化 → 炎症小体过度激活
LPIN2 缺陷 → 巨噬细胞炎症反应失调

### 3.2 关键治疗靶点
| 靶点 | 药物 | 机制 | 临床阶段 |
|------|------|------|----------|
| IL-1β | Anakinra | IL-1受体拮抗剂 | 已获批用于PAPA |
| TNF-α | 阿达木单抗 | TNF抑制剂 | 超说明书使用 |
| IL-17 | 司库奇尤单抗 | IL-17A抑制剂 | 临床研究 |
| JAK | 托法替布 | JAK抑制剂 | 病例报告有效 |

## 四、外部数据库资源
| 数据库 | URL | 用途 |
|--------|-----|------|
| ClinVar | ncbi.nlm.nih.gov/clinvar | 已知变异致病性注释 |
| OMIM | omim.org | 基因-疾病关联权威数据库 |
| gnomAD | gnomad.broadinstitute.org | 人群变异频率数据库 |
| GEO | ncbi.nlm.nih.gov/geo | 基因表达数据集 |
| UniProt | uniprot.org | 蛋白质功能注释 |
| PubMed | pubmed.ncbi.nlm.nih.gov | 文献检索 |
| STRING | string-db.org | 蛋白质互作网络 |
| OpenTargets | opentargets.org | 靶点-疾病关联 |

## 五、竞赛与基金机会速查
| 来源类型 | 平台/机构 | 更新频率 | 典型奖金 | SAPHO匹配度 |
|----------|----------|----------|----------|------------|
| Kaggle竞赛 | kaggle.com | 持续 | $5k-$100k | ★★★★ |
| 阿里云天池 | tianchi.aliyun.com | 季度 | 5万-50万CNY | ★★★ |
| 罕见病科研基金 | 科技部/卫健委 | 年度 | 50万-500万CNY | ★★★★★ |
| GitHub Sponsors | github.com | 持续 | 不定 | ★★★★ |
| SCI论文奖励 | 各医院/学校 | 持续 | 1万-20万CNY | ★★★★ |
| 中国罕见病联盟 | chard.org.cn | 年度 | 10万-30万CNY | ★★★★ |

## 六、参考文献
1. Li C, et al. SAPHO syndrome: current clinical, diagnostic and treatment approaches. Rheumatology. 2021.
2. Zhang Y, et al. IL36RN mutations in Chinese SAPHO patients. J Transl Med. 2022.
3. Marzano AV, et al. SAPHO syndrome: a review of pathogenetic concepts. Br J Dermatol. 2023.
4. Wang X, et al. LPIN2 mutations in early-onset SAPHO/CRMO patients. Pediatr Rheumatol. 2023.
5. Genovese G, et al. New insights into the pathogenesis of SAPHO syndrome. JEADV. 2022.
