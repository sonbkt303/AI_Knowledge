#!/usr/bin/env python3
"""Simple scraper to fetch VN-Index, HNX, UPCoM summary from vietstock.vn.

This script is best-effort: public site structure may change. It writes a small
JSON file under reports/ when successful.
"""
import json
import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup


URL = "https://vietstock.vn/"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; Bot/1.0)"}
TARGETS = ["VN-Index", "HNX-Index", "UPCoM"]


def parse_number(text: str):
    if text is None:
        return None
    t = text.replace(',', '').strip()
    m = re.search(r"-?\d{1,3}(?:\.?\d+)?", t)
    if not m:
        return None
    try:
        return float(m.group(0))
    except Exception:
        return None


def find_index_data(soup, name):
    # find element that contains the name text
    el = soup.find(string=re.compile(re.escape(name), re.I))
    if not el:
        return None
    parent = el.parent
    # search nearby for numbers
    # look for next siblings and parent's descendants
    text_candidates = []
    for tag in parent.find_all(text=True, limit=20):
        text_candidates.append(tag.strip())
    for sib in parent.find_next_siblings(limit=6):
        text_candidates.extend([t.strip() for t in sib.find_all(text=True, limit=10)])
    # try to extract price and change
    price = None
    pct = None
    for txt in text_candidates:
        if price is None:
            v = parse_number(txt)
            if v is not None:
                price = v
                continue
        # percentage
        if pct is None and '%' in (txt or ''):
            try:
                pct = float(txt.replace('%', '').replace('+', '').replace(',', '').strip())
            except Exception:
                pct = None
    return {"name": name, "price": price, "pct": pct}


def scrape():
    resp = requests.get(URL, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    results = {}
    for t in TARGETS:
        data = find_index_data(soup, t)
        results[t] = data
    return results


def main():
    out = Path("reports")
    out.mkdir(parents=True, exist_ok=True)
    try:
        res = scrape()
    except Exception as e:
        print("Scrape failed:", e, file=sys.stderr)
        sys.exit(1)
    path = out / "vietstock-summary.json"
    path.write_text(json.dumps(res, indent=2, ensure_ascii=False), encoding="utf-8")
    print("Wrote:", path)


if __name__ == '__main__':
    main()
