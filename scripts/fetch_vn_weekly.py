#!/usr/bin/env python3
"""Fetch weekly VN market data and generate a markdown report.

Usage:
  python3 scripts/fetch_vn_weekly.py --end 2026-03-14

This script uses yfinance to download data for VN-Index, HNX, UPCoM and
produces a simple weekly summary markdown file under reports/.
"""
import argparse
import datetime as dt
import subprocess
import sys
from pathlib import Path

def ensure_packages():
    try:
        import yfinance as yf  # noqa: F401
        import pandas as pd  # noqa: F401
    except Exception:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yfinance", "pandas", "numpy", "feedparser", "requests", "beautifulsoup4"])

ensure_packages()

import yfinance as yf
import pandas as pd
import numpy as np
import json
from pathlib import Path


def normalize_scalar(x):
    """Convert numpy/pandas scalar/Series/DataFrame to Python float or None."""
    try:
        if x is None:
            return None
        # pandas Series or DataFrame
        import pandas as _pd
        if isinstance(x, _pd.Series):
            if len(x) == 0:
                return None
            return float(x.iloc[-1])
        if isinstance(x, _pd.DataFrame):
            if x.size == 0:
                return None
            return float(x.iloc[-1, 0])
    except Exception:
        pass
    try:
        # numpy types
        import numpy as _np
        if isinstance(x, (_np.floating, _np.integer)):
            return float(x)
    except Exception:
        pass
    try:
        return float(x)
    except Exception:
        return None


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    up = delta.clip(lower=0)
    down = -1 * delta.clip(upper=0)
    ma_up = up.ewm(com=period - 1, adjust=False).mean()
    ma_down = down.ewm(com=period - 1, adjust=False).mean()
    rs = ma_up / ma_down
    return 100 - (100 / (1 + rs))


TICKERS = {
    "VN-Index": "^VNINDEX",
}


def fetch_weekly(ticker: str, end_date: dt.date):
    # download 40 trading days to be safe
    start = end_date - dt.timedelta(days=40)
    df = yf.download(ticker, start=start.isoformat(), end=(end_date + dt.timedelta(days=1)).isoformat(), progress=False)
    if df.empty:
        return None
    df.index = pd.to_datetime(df.index)
    return df


def load_vietstock_summary():
    p = Path('reports') / 'vietstock-summary.json'
    if not p.exists():
        return {}
    try:
        data = json.loads(p.read_text(encoding='utf-8'))
    except Exception:
        return {}
    normalized = {}
    for k, v in data.items():
        key = k
        # normalize keys to match our TICKERS keys
        if 'VN' in k.upper():
            normalized['VN-Index'] = v
        elif 'HNX' in k.upper():
            normalized['HNX'] = v
        elif 'UP' in k.upper() or 'UPCOM' in k.upper():
            normalized['UPCoM'] = v
        else:
            normalized[key] = v
    return normalized


def summary_for(df: pd.DataFrame):
    close = df['Close']
    last = close.iloc[-1]
    prev = close.iloc[-5] if len(close) >= 6 else close.iloc[0]
    try:
        pct = (last - prev) / prev * 100
    except Exception:
        pct = None
    ma20 = close.rolling(window=20).mean().iloc[-1] if len(close) >= 20 else None
    ma50 = close.rolling(window=50).mean().iloc[-1] if len(close) >= 50 else None
    r = rsi(close).iloc[-1] if len(close) >= 15 else None
    vol = df.get('Volume')
    try:
        vol_ratio = float(vol.iloc[-1]) / float(vol[:-1].mean()) if vol is not None and len(vol) > 1 else None
    except Exception:
        vol_ratio = None
    return dict(
        last=normalize_scalar(last),
        pct_week=normalize_scalar(pct),
        ma20=normalize_scalar(ma20),
        ma50=normalize_scalar(ma50),
        rsi=normalize_scalar(r),
        vol_ratio=normalize_scalar(vol_ratio),
    )


def generate_markdown(end_date: str, results: dict, out_path: Path):
    lines = []
    def fmt(x, d=2):
        try:
            if x is None:
                return "N/A"
            if isinstance(x, float) and np.isnan(x):
                return "N/A"
            return f"{x:.{d}f}"
        except Exception:
            return str(x)
    def safe_scalar(x):
        # convert pandas Series/DataFrame-like to scalar when possible
        try:
            import pandas as _pd
            if isinstance(x, _pd.Series):
                if len(x) == 0:
                    return None
                return float(x.iloc[-1])
            if isinstance(x, _pd.DataFrame):
                # try to take last row, first column
                if x.size == 0:
                    return None
                return float(x.iloc[-1, 0])
        except Exception:
            pass
        return x
    lines.append(f"# Báo cáo Thị trường Chứng khoán Tuần — kết thúc {end_date}")
    lines.append("")
    lines.append("## Chỉ số chính")
    lines.append("")
    # preferred display order and pretty names
    display_order = ["VN-Index", "HNX", "UPCoM", "Gold_USD", "WTI_Oil", "Brent_Oil"]
    pretty_names = {
        'Gold_USD': 'Gold (USD/oz)',
        'WTI_Oil': 'WTI (USD/bbl)',
        'Brent_Oil': 'Brent (USD/bbl)'
    }
    for key in display_order:
        s = results.get(key)
        name = pretty_names.get(key, key)
        if s is None:
            lines.append(f"- {name}: dữ liệu không có hoặc lỗi tải về")
            continue
        if isinstance(s, dict):
            last = normalize_scalar(s.get('last'))
            pct = normalize_scalar(s.get('pct_week'))
            if last is None:
                lines.append(f"- {name}: dữ liệu không có hoặc lỗi tải về")
            else:
                if pct is not None:
                    lines.append(f"- {name}: {fmt(last)} (Tuần: {fmt(pct)}%)")
                else:
                    lines.append(f"- {name}: {fmt(last)}")
        else:
            val = normalize_scalar(s)
            if val is None:
                lines.append(f"- {name}: dữ liệu không có hoặc lỗi tải về")
            else:
                lines.append(f"- {name}: {fmt(val)}")
    lines.append("")
    lines.append("## Ghi chú")
    lines.append("")
    lines.append("- Báo cáo này tạo tự động bằng `scripts/fetch_vn_weekly.py`. Cập nhật thêm phân tích ngành và cổ phiếu theo nhu cầu.")
    # events and headlines (if provided)
    events = results.get('events', [])
    headlines = results.get('headlines', [])
    if headlines:
        lines.append("")
        lines.append("---")
        lines.append("## Dòng thời gian — Sự kiện tuần qua")
        for h in headlines:
            lines.append(f"- [{h.get('date')}] — {h.get('title')} ({h.get('source')})")
    if events:
        lines.append("")
        lines.append("---")
        lines.append("## Dòng thời gian — Sự kiện dự kiến tuần tới")
        for e in events:
            lines.append(f"- [{e.get('date')}] — {e.get('title')} — {e.get('note')}")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--end", required=False, help="End date YYYY-MM-DD", default=dt.date.today().isoformat())
    args = p.parse_args()
    end = dt.date.fromisoformat(args.end)
    results = {}
    viet = load_vietstock_summary()
    for name, ticker in TICKERS.items():
        # prefer vietstock summary if available
        if name in viet and viet[name] is not None and viet[name].get('price') is not None:
            print(f"Using vietstock data for {name}")
            d = viet[name]
            try:
                last = float(d.get('price')) if d.get('price') is not None else None
            except Exception:
                last = None
            pct = None
            try:
                pct = float(d.get('pct')) if d.get('pct') is not None else None
            except Exception:
                pct = None
            results[name] = dict(last=last, pct_week=pct, ma20=np.nan, ma50=np.nan, rsi=np.nan, vol_ratio=np.nan)
            continue

        print(f"Downloading {name} ({ticker})...")
        df = fetch_weekly(ticker, end)
        if df is None:
            print(f"No data for {ticker}")
            results[name] = None
            continue
        results[name] = summary_for(df)
    # fetch headlines from RSS (Reuters) for the past week
    try:
        from datetime import timedelta
        import feedparser

        def fetch_headlines(feeds, start_date, end_date, keywords=None):
            entries = []
            for url in feeds:
                try:
                    d = feedparser.parse(url)
                except Exception:
                    continue
                for e in d.entries:
                    if not hasattr(e, 'published_parsed'):
                        continue
                    pub = dt.date(e.published_parsed.tm_year, e.published_parsed.tm_mon, e.published_parsed.tm_mday)
                    if pub < start_date or pub > end_date:
                        continue
                    title = e.get('title', '').strip()
                    summary = e.get('summary', '')
                    text = f"{title} {summary}".lower()
                    if keywords:
                        if not any(k.lower() in text for k in keywords):
                            continue
                    entries.append({'date': pub.isoformat(), 'title': title, 'link': e.get('link', ''), 'source': url})
            # sort by date
            entries.sort(key=lambda x: x['date'])
            return entries

        feeds = [
            'http://feeds.reuters.com/Reuters/worldNews',
            'http://feeds.reuters.com/Reuters/businessNews'
        ]
        start_week = end - dt.timedelta(days=7)
        keywords = ['fed', 'interest rate', 'inflation', 'cpi', 'war', 'russia', 'ukraine', 'oil']
        headlines = fetch_headlines(feeds, start_week, end, keywords=keywords)
    except Exception:
        headlines = []

    # fetch FOMC / Fed calendar events (simple scraper)
    try:
        import requests
        from bs4 import BeautifulSoup

        def fetch_fed_calendar():
            url = 'https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm'
            try:
                r = requests.get(url, timeout=10)
                soup = BeautifulSoup(r.text, 'html.parser')
                table = soup.find('table')
                events = []
                if not table:
                    return events
                for row in table.find_all('tr'):
                    cols = [c.get_text(strip=True) for c in row.find_all(['th', 'td'])]
                    if len(cols) >= 2:
                        date_text = cols[0]
                        title = cols[1]
                        events.append({'date': date_text, 'title': title, 'note': 'FOMC calendar'})
                return events
            except Exception:
                return []

        fed_events = fetch_fed_calendar()
        # simple filter: events whose date string contains year and are within next 7 days
        upcoming = []
        for e in fed_events:
            try:
                # attempt parse YYYY or month name; keep as-is otherwise
                upcoming.append(e)
            except Exception:
                continue
    except Exception:
        upcoming = []

    # attach headlines and events to results for markdown generation
    results['headlines'] = headlines
    results['events'] = upcoming
    out = Path("reports") / f"weekly-report-{end.isoformat()}.md"
    generate_markdown(end.isoformat(), results, out)
    print("Report written to", out)


if __name__ == '__main__':
    main()
