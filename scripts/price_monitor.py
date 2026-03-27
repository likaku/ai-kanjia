#!/usr/bin/env python3
"""
静默谈判官 - 价格监控脚本
功能：抓取商品价格、搜索竞品最低价、检测优惠券
"""

import json
import re
from datetime import datetime
from pathlib import Path

MEMORY_DIR = Path.home() / "WorkBuddy" / "20260327224320" / ".workbuddy" / "memory"
PRICE_LOG = MEMORY_DIR / "price_history.jsonl"

def log_price(product_id, product_name, price, source):
    """记录价格到历史日志"""
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    entry = {
        "timestamp": datetime.now().isoformat(),
        "product_id": product_id,
        "product_name": product_name,
        "price": price,
        "source": source
    }
    with open(PRICE_LOG, "a") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry

def get_price_history(product_id, limit=10):
    """获取商品价格历史"""
    if not PRICE_LOG.exists():
        return []
    history = []
    with open(PRICE_LOG) as f:
        for line in f:
            entry = json.loads(line)
            if entry.get("product_id") == product_id:
                history.append(entry)
    return history[-limit:]

def analyze_price_trend(product_id):
    """分析价格趋势"""
    history = get_price_history(product_id)
    if len(history) < 2:
        return {"trend": "unknown", "change": 0, "change_pct": 0}

    latest = history[-1]["price"]
    oldest = history[0]["price"]
    change = latest - oldest
    change_pct = (change / oldest * 100) if oldest > 0 else 0

    return {
        "trend": "down" if change < 0 else "up" if change > 0 else "stable",
        "change": change,
        "change_pct": round(change_pct, 2),
        "lowest": min(h["price"] for h in history),
        "highest": max(h["price"] for h in history)
    }

def parse_price_from_text(text):
    """从文本中提取价格"""
    patterns = [
        r'[¥￥](\d+(?:\.\d{1,2})?)',
        r'RMB\s*(\d+(?:\.\d{1,2})?)',
        r'价格[：:]\s*(\d+(?:\.\d{1,2})?)',
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return float(match.group(1))
    return None

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: price_monitor.py <product_id> <price> [product_name]")
        sys.exit(1)

    product_id = sys.argv[1]
    price = float(sys.argv[2])
    product_name = sys.argv[3] if len(sys.argv) > 3 else "Unknown"

    result = log_price(product_id, product_name, price, "manual")
    print(f"✅ 价格已记录: {product_name} = ¥{price}")
    print(f"   时间: {result['timestamp']}")