---
name: 爱砍价
description: |
  智能砍价助手。当用户提到"议价"、"砍价"、"找优惠"、"价格监控"、"自动降价提醒"、"旺旺议价"、"购物车价格保护"时使用此技能。
  利用高频价格检索与卖家Agent进行非同步价格博弈，自动发起"基于证据的议价"，实现价格自动最优化。
  支持马云体/Lucas体风格话术，让砍价更有感染力！
  与淘宝桌面客户端深度整合，支持SKU规格议价、购物车议价、订单议价等完整流程。
  可预估每次议价节省金额，实现"价格自动最优化"。
---

# 🛒 爱砍价 (AI Negotiator)

> AI智能砍价助手 - 让每一次议价都更有感染力！
>
> **核心逻辑**: 利用 CLI 的高频检索能力与卖家的"客服 Agent"进行非同步的价格博弈。
>
> Copyright (c) 2026 kaku. All rights reserved.

---

## 🎯 核心能力

1. **价格监控** - 监控收藏夹/购物车商品，发现竞品降价时自动议价
2. **竞品比价** - 抓取全网同款历史最低价（通过 MCP 读取第三方比价数据）
3. **SKU感知议价** - 根据商品规格定制议价话术
4. **优惠券检测** - 检测店铺"老客优惠"或"隐藏券"
5. **旺旺议价** - 自动通过 CLI 调用旺旺接口，发起"基于证据的议价"
6. **省钱预估** - 预判每次议价可节省金额

---

## 🔗 淘宝Native整合

本Skill与 `taobao-native` CLI深度整合：

### 自动化路径

```
┌─────────────────────────────────────────────────────────────────┐
│  1. 抓取全网同款历史最低价 (search_products / MCP比价数据)        │
├─────────────────────────────────────────────────────────────────┤
│  2. 检测店铺"老客优惠"或"隐藏券" (scan_page_elements)           │
├─────────────────────────────────────────────────────────────────┤
│  3. 获取商品SKU信息 (get_product_skus)                           │
├─────────────────────────────────────────────────────────────────┤
│  4. 生成针对性话术 (Lucas体/马云体)                              │
├─────────────────────────────────────────────────────────────────┤
│  5. 自动发送旺旺消息 (open_chat)                                 │
├─────────────────────────────────────────────────────────────────┤
│  6. 预估省钱金额 → 记录议价结果                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 典型话术

```
"您好，我看到同款在 XX 平台价格更低，如果能匹配价格或提供 10 元无门槛券，我立刻下单。"
```

---

## 💰 省钱预估模型

| 商品类型 | 预估节省比例 | 典型节省金额 |
|---------|-------------|-------------|
| 生鲜食品 | 5-15% | ¥5-20 |
| 服装鞋帽 | 10-25% | ¥10-50 |
| 数码电子 | 3-8% | ¥20-100 |
| 家居日用 | 8-15% | ¥5-30 |
| 大额订单(>¥500) | 5-10% | ¥25-100 |

**个人价值**: 无需亲自沟通，实现"价格自动最优化"。

---

## 🎭 预设场景与话术风格

### 场景1: 竞品比价型 (P0优先级)
**触发条件**: 发现同款其他平台价格更低
**话术风格**: Lucas体 - 逻辑清晰、数据驱动
**预估节省**: ¥5-30

```
您好，我对比了同款商品：
- 贵店价格：¥XXX
- XX平台价格：¥XXX（低¥XX）

如果贵店能匹配价格或提供XX元优惠券，我立刻下单。
期待您的回复！
```

### 场景2: 老客户专属型 (P1优先级)
**触发条件**: 复购用户/收藏店铺
**话术风格**: Lucas体 + 马云体 - 情感+逻辑
**预估节省**: ¥5-15

```
您好，我是贵店的老客户了（已收藏）。
看到别家有活动，但更愿意支持你们的服务。
请问有老客户专属优惠吗？哪怕少一点点，我立刻下单！
```

### 场景3: SKU规格议价型 (P1优先级)
**触发条件**: 不同规格价格差异大
**话术风格**: Lucas体 - 规格对比
**预估节省**: ¥10-30

```
您好，我对比了规格价格：
- 贵店大号(6-8钱)：¥XXX
- XX平台同款中号：¥XXX

如果能申请一个老客户价，我愿意升规格购买！
```

### 场景4: 批量采购型 (P2优先级)
**触发条件**: 购买数量≥3件
**话术风格**: 马云体 - 豪爽直接
**预估节省**: ¥20-100

```
老板！爽快人不说暗话——
我需要采购X份，能给个批发价吗？
价格合适我立刻付款，以后长期合作！
```

### 场景5: 限时紧迫型 (P2优先级)
**触发条件**: 节日大促/库存紧张
**话术风格**: Lucas体 + 紧迫
**预估节省**: ¥5-20

```
您好，看到XX平台在做活动（价格更低）。
如果贵店能再优惠X元，我今天立刻下单！
```

### 场景6: 价格保护型 (P3优先级)
**触发条件**: 下单后7天内发现降价
**话术风格**: Lucas体 - 理性协商
**预估节省**: ¥10-50

```
您好，我X月X日在贵店购买了XX（订单号：XXX），
今天发现同款降价了¥XX。
请问可以申请价格保护或退差价吗？
```

---

## 🎨 话术风格对比

### Lucas体特点
- 逻辑清晰，数据驱动
- 结构化表达
- 专业但不失温度
- 适合：比价、价格保护、批量采购

### 马云体特点
- 反问句多、感叹句多
- 口语化、接地气
- 情感共鸣强
- 适合：老客户议价、紧急促单

---

## 📊 议价效果追踪

```markdown
## [日期] 议价统计
- 总议价次数: X
- 成功次数: X (成功率: XX%)
- 总节省金额: ¥XXX
- 平均每单节省: ¥XX

### 成功案例
- 商品A: 原价¥XXX → 成交价¥XXX (省¥XX)
- 商品B: 原价¥XXX → 成交价¥XXX (省¥XX)
```

---

## 📝 License

```
Copyright (c) 2026 kaku. All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

Made with ❤️ by [kaku](https://github.com/likaku)