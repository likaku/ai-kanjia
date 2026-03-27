---
name: 爱砍价
description: |
  智能砍价助手。当用户提到"议价"、"砍价"、"找优惠"、"价格监控"、"自动降价提醒"、"旺旺议价"、"购物车价格保护"时使用此技能。
  利用高频价格检索与卖家Agent进行非同步价格博弈，自动发起"基于证据的议价"，实现价格自动最优化。
  支持马云体风格话术，让砍价更有感染力！
  与淘宝桌面客户端深度整合，支持SKU规格议价、购物车议价、订单议价等完整流程。
---

# 爱砍价 (AI Negotiator)

> AI智能砍价助手 - 让每一次议价都更有感染力！
>
> Copyright (c) 2026 kaku. All rights reserved.

---

## 🔗 淘宝Native整合

本Skill与 `taobao-native` CLI深度整合，实现完整的议价流程：

### SKU议价流程

```python
# Step 1: 获取商品SKU信息
taobao-native get_product_skus --args '{"itemId": "<商品ID>", "sourceApp": "workbuddy"}'

# Step 2: 根据SKU生成针对性话术
# 大号/中号/小号 - 不同规格有不同议价空间

# Step 3: 加入购物车
taobao-native add_to_cart --args '{"itemId": "<商品ID>", "sku": ["大号6-8钱"], "sourceApp": "workbuddy"}'

# Step 4: 从购物车发起议价
taobao-native open_chat --args '{"source": "cart", "productName": "小龙虾", "message": "..."}'
```

### 议价场景分类

| 场景 | 工具链 | 话术重点 |
|------|--------|---------|
| SKU规格选择 | `get_product_skus` → `add_to_cart` | 根据规格大小调整议价幅度 |
| 购物车批量议价 | `navigate cart` → `open_chat` | 批量商品打包议价 |
| 订单完成后议价 | `open_chat` from order | 申请价格保护 |
| 收藏夹商品议价 | `get_browse_history` → `open_chat` | 表明复购意向 |

---

## 核心能力

1. **价格监控** - 追踪购物车/收藏夹商品价格变化
2. **竞品比价** - 全网同款商品历史最低价抓取
3. **SKU感知议价** - 根据商品规格定制议价话术
4. **优惠券检测** - 监测店铺隐藏优惠券/老客价
5. **旺旺议价** - 自动发送证据化议价话术

---

## 工作流程

### Step 1: 商品情报收集

```python
# 使用 taobao-native 获取商品信息
taobao-native navigate_to_url --args '{"url": "<商品URL>", "sourceApp": "workbuddy"}'
taobao-native get_product_skus --args '{"itemId": "<商品ID>", "sourceApp": "workbuddy"}'
```

### Step 2: 价格情报收集

```python
# 参考 scripts/price_monitor.py
- 抓取商品当前价格
- 分析SKU规格对应的价格区间
- 搜索同款全网最低价 (通过search_products)
- 检测店铺优惠券 (通过旺旺接口)
- 记录价格历史到 memory/
```

### Step 3: 议价触发条件

| 触发条件 | 优先级 | 议价策略 |
|---------|-------|---------|
| 竞品价格更低 | P0 | 发同款链接，要求匹配 |
| 发现隐藏优惠券 | P1 | 直接询问优惠 |
| **SKU规格价格差异** | P1 | 根据规格大小调整议价目标 |
| 老客户专属价 | P2 | 表明复购意向 |
| 价格上涨前兆 | P3 | 提醒并建议入手 |

### Step 4: 发送议价话术

典型话术模板：
```
"您好，我看到同款[大号6-8钱]在XX平台价格更低（XX元），
如果能匹配价格或提供XX元无门槛券，我立刻下单。"
```

---

## SKU话术模板

### 规格降级型（大改小）
```
您好，我看到XX平台同款[中号4-6钱]只要XX元，比你们便宜XX元。
说实话，你们的大号品质确实更好，但价格差距有点大。
能不能申请一个老客户价？哪怕少10块，我马上下单！
```

### 规格升级型（小改大）
```
您好，我是老客户了，看到你们大号6-8钱的性价比不错。
说实话XX平台中号才卖XX元，你们能帮忙申请一个优惠吗？
如果价格合适，我愿意升规格买大号！
```

### 批量采购型
```
您好，我看到你们有[中号4-6钱]的规格，我想采购X份。
请问有批发价吗？或者可以申请什么优惠？
```

---

## 议价话术库（完整版）

详见 `references/talk_tracks.md`

---

## 输出格式

每次议价后记录到当日memory文件：

```markdown
## [时间] 议价记录
- 商品: [商品名称] - [SKU规格]
- 原价: ¥XX
- SKU规格: [具体规格]
- 竞品价: ¥XX
- 议价结果: [成功/失败/待回复]
- 卖家回复: [回复内容]
- 节省: ¥XX
```

---

## 注意事项

- **SKU优先**：议价前必须先获取商品SKU信息，根据规格定制话术
- 每次只针对1-2款商品议价，避免骚扰卖家
- 同一商品48小时内不重复议价
- 议价成功记录到 MEMORY.md 的"议价成功案例"区
- 保持话术自然，避免机器人感过强

---

## 相关文件

- 议价话术模板: `references/talk_tracks.md`
- 价格监控脚本: `scripts/price_monitor.py`
- 议价记录脚本: `scripts/log_negotiation.py`

---

## 📝 License & Copyright

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