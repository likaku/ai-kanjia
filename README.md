# 🛒 爱砍价 (AI Haggler)

> AI智能砍价助手 - 让每一次议价都更有感染力！

[![Apache 2.0 License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![GitHub Stars](https://img.shields.io/github/stars/likaku/ai-kanjia?style=social)](https://github.com/likaku/ai-kanjia)

---

## 🚀 工作流程

分析购物车，找到最合适砍价的商品

<img width="831" height="239" alt="Clipboard_Screenshot_1774629893" src="https://github.com/user-attachments/assets/4ffb2413-f94d-4fb4-ad9d-4bf338a8b715" />

设计话术

<img width="833" height="290" alt="Clipboard_Screenshot_1774629922" src="https://github.com/user-attachments/assets/f4102370-e8d3-4356-ade5-c0c95ee521a5" />

发送消息沟通

<img width="642" height="248" alt="Clipboard_Screenshot_1774629980" src="https://github.com/user-attachments/assets/976d9642-b866-4bd6-8850-8dac69cbc8d5" />

放入清单进行下一步沟通

<img width="843" height="169" alt="Clipboard_Screenshot_1774629942" src="https://github.com/user-attachments/assets/1fddc3d2-651f-435f-b0d6-9cc07701d8a2" />

---

## ✨ 核心功能

<p align="center">
  <img src="https://img.shields.io/badge/🔍-价格监控-FF6B6B?style=for-the-badge" />
  <img src="https://img.shields.io/badge/💰-竞品比价-4ECDC4?style=for-the-badge" />
  <img src="https://img.shields.io/badge/🎫-优惠券检测-FFE66D?style=for-the-badge" />
  <img src="https://img.shields.io/badge/💬-旺旺议价-95E1D3?style=for-the-badge" />
  <img src="https://img.shields.io/badge/🎭-马云体话术-F38181?style=for-the-badge" />
</p>

| 功能 | 说明 |
|:---|:---|
| 🔍 **价格监控** | 追踪购物车/收藏夹商品价格变化 |
| 💰 **竞品比价** | 全网同款商品历史最低价抓取 |
| 🎫 **优惠券检测** | 监测店铺隐藏优惠券/老客价 |
| 💬 **旺旺议价** | 自动发送证据化议价话术 |
| 🎭 **马云体话术** | 反问+感叹+口语化，更有感染力 |

---

## 📦 安装

```bash
# 克隆仓库
git clone https://github.com/likaku/ai-kanjia.git

# 安装依赖
cd ai-kanjia
pip install -r requirements.txt
```

---

## 💬 话术示例

### 马云体风格

```
老板！跟您说句心里话——

我认真比较了一圈，同款鲜活小龙虾3斤大号6-8钱的，别家便宜了8块钱，我心里有数。

但是说实话，我还是想跟您买。为什么？因为你们发货快、服务好、评价也实在。

所以我就想问您一句——
您这边能不能帮我申请一个老客户价？
哪怕少10块20块的，我马上付款，而且以后买小龙虾就认准你们家了。

我跟您讲，我现在就差这一步，您要是能帮我这个忙，我立刻下单，绝不犹豫！

您看，这事儿能不能成？
```

### 适用场景

| 场景 | 示例 |
|:---|:---|
| 🏷️ **发现同款低价** | "我看到XX平台才卖XX元，能匹配吗？" |
| 👴 **老客户议价** | "我收藏了两次了，能给个老客价吗？" |
| 📦 **批量采购** | "我要买3份，批发价能多少？" |
| ⏰ **限时紧迫** | "今天活动最后一天，能再优惠吗？" |

---

## 📁 项目结构

```
ai-kanjia/
├── SKILL.md                      # Skill 核心定义
├── README.md                     # 项目说明文档
├── requirements.txt               # Python 依赖
├── references/
│   └── talk_tracks.md           # 马云体话术模板库
└── scripts/
    ├── price_monitor.py         # 价格监控脚本
    └── log_negotiation.py       # 议价记录脚本
```

---

## 🚀 产品路线图

| 版本 | 阶段 | 核心能力 |
|:---|:---:|:---|
| **v1.0** | ✅ | 话术驱动的旺旺议价（马云体） |
| **v1.5** | 🔜 | 跨平台电商整合（拼多多/京东/抖音） |
| **v2.0** | 🔜 | Clean Sheet 成本拆解分析 |
| **v2.5** | 🔜 | 上下游供应链分析 |
| **v3.0** | 🔜 | Kraljic 矩阵策略分类 |
| **v3.5** | 🔜 | AI Agent 全自动深度议价 |

### v1.5 跨平台覆盖

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   ✅ 淘宝/天猫        🔜 拼多多         🔜 京东          │
│                                                         │
│   🔜 抖音/快手        🔜 唯品会         🔜 ...         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### v2.0+ Clean Sheet 成本拆解

```
商品零售价 = 原材料成本 + 加工成本 + 物流成本
           + 营销费用 + 品牌溢价 + 利润空间

原材料成本 = 大宗商品价格 × 用量 × 损耗率
```

| 分析维度 | 说明 |
|:---|:---|
| 🏭 **Clean Sheet** | 大宗商品价格 → 原材料成本估算 |
| 📈 **周期分析** | 原材料价格与成品价的传导关系 |
| 🔗 **上下游** | 供应链利润分配分析 |
| 📊 **Kraljic** | 战略型/杠杆型/瓶颈型/routine 分类 |

---

## 💰 预期收益

| 版本 | 单次议价节省 | 年化节省（按10次/月）|
|:---|:---:|:---:|
| v1.0 | ¥5-30 | ¥600-3,600 |
| v1.5 | ¥10-50 | ¥1,200-6,000 |
| v2.0+ | ¥30-100 | ¥3,600-12,000 |

---

## 🎯 使用流程

```
输入商品链接
     │
     ▼
┌─────────────┐
│ 1. 价格抓取  │ ──→ 全网同款历史最低价
└─────────────┘
     │
     ▼
┌─────────────┐
│ 2. 优惠检测  │ ──→ 隐藏优惠券/老客价
└─────────────┘
     │
     ▼
┌─────────────┐
│ 3. 话术生成  │ ──→ 马云体风格定制
└─────────────┘
     │
     ▼
┌─────────────┐
│ 4. 旺旺发送  │ ──→ 自动发送议价消息
└─────────────┘
     │
     ▼
  📊 预估节省 ¥10-30
```

---

## 📜 License

Apache License 2.0 - 永久免费开源

---

<div align="center">

**Made with ❤️ by [kaku](https://github.com/likaku)**

⭐ Star this repo if you find it helpful!

</div>
