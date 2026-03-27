#!/usr/bin/env python3
"""
静默谈判官 - 议价记录脚本
功能：记录每次议价的结果，用于追踪和优化
"""

import json
from datetime import datetime
from pathlib import Path

MEMORY_DIR = Path.home() / "WorkBuddy" / "20260327224320" / ".workbuddy" / "memory"
NEGOTIATION_LOG = MEMORY_DIR / "negotiations.jsonl"

def log_negotiation(
    product_id: str,
    product_name: str,
    original_price: float,
    competitor_price: float = None,
    coupon_found: float = None,
    result: str = "pending",  # success/failed/pending/no_response
    seller_reply: str = None,
    final_price: float = None,
    savings: float = None,
    talk_track: str = None
):
    """
    记录一次议价尝试

    Args:
        product_id: 商品ID
        product_name: 商品名称
        original_price: 原始价格
        competitor_price: 竞品价格（如果有）
        coupon_found: 发现的优惠券金额（如果有）
        result: 议价结果
        seller_reply: 卖家回复
        final_price: 最终价格
        savings: 节省金额
        talk_track: 使用的话术模板
    """
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

    entry = {
        "timestamp": datetime.now().isoformat(),
        "product_id": product_id,
        "product_name": product_name,
        "original_price": original_price,
        "competitor_price": competitor_price,
        "coupon_found": coupon_found,
        "result": result,
        "seller_reply": seller_reply,
        "final_price": final_price,
        "savings": savings,
        "talk_track": talk_track
    }

    with open(NEGOTIATION_LOG, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    return entry

def get_negotiation_history(product_id=None, limit=20):
    """获取议价历史"""
    if not NEGOTIATION_LOG.exists():
        return []

    history = []
    with open(NEGOTIATION_LOG) as f:
        for line in f:
            entry = json.loads(line)
            if product_id is None or entry.get("product_id") == product_id:
                history.append(entry)

    return history[-limit:]

def get_success_rate():
    """计算议价成功率"""
    history = get_negotiation_history(limit=1000)
    if not history:
        return {"total": 0, "success": 0, "rate": 0}

    total = len(history)
    success = len([h for h in history if h.get("result") == "success"])

    return {
        "total": total,
        "success": success,
        "rate": round(success / total * 100, 1) if total > 0 else 0,
        "total_savings": sum(h.get("savings", 0) for h in history if h.get("savings"))
    }

def format_negotiation_report(product_id=None):
    """格式化议价报告"""
    history = get_negotiation_history(product_id)
    stats = get_success_rate()

    report = f"""## 议价报告

### 统计数据
- 总议价次数: {stats['total']}
- 成功次数: {stats['success']}
- 成功率: {stats['rate']}%
- 总节省: ¥{stats.get('total_savings', 0):.2f}

### 最近议价记录
"""

    for h in history[-5:]:
        emoji = "✅" if h["result"] == "success" else "❌" if h["result"] == "failed" else "⏳"
        report += f"""
{emoji} **{h['product_name']}**
- 原价: ¥{h['original_price']}
- 结果: {h['result']}
- 卖家回复: {h.get('seller_reply', '无')}
- 节省: ¥{h.get('savings', 0) or 0:.2f}
"""

    return report

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage: log_negotiation.py <product_id> <product_name> <original_price>")
        sys.exit(1)

    product_id = sys.argv[1]
    product_name = sys.argv[2]
    original_price = float(sys.argv[3])

    entry = log_negotiation(
        product_id=product_id,
        product_name=product_name,
        original_price=original_price,
        result="pending"
    )
    print(f"✅ 议价记录已创建: {product_name}")
    print(f"   时间: {entry['timestamp']}")