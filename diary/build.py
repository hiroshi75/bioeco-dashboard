#!/usr/bin/env python3
"""Static site generator for BioEco Research Diary.

Generates:
  - diary.html          (latest 20 entries + archive links)
  - diary/YYYY-MM.html  (monthly archive pages)

Run after adding a new entry:
    python3 workspace/website/diary/build.py
"""
import json
import os
import re
import html
from collections import defaultdict
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.dirname(SCRIPT_DIR)
ENTRIES_PATH = os.path.join(SCRIPT_DIR, 'entries.jsonl')
MAX_RECENT = 20

CSS = """\
:root { --bg: #0a0f1a; --card: #111827; --border: #1e293b; --accent: #10b981; --accent2: #3b82f6; --text: #e2e8f0; --dim: #94a3b8; --red: #ef4444; --yellow: #f59e0b; }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Inter', -apple-system, sans-serif; background: var(--bg); color: var(--text); line-height: 1.7; }
.container { max-width: 800px; margin: 0 auto; padding: 0 20px; }
header { background: linear-gradient(135deg, #064e3b 0%, #0f172a 100%); padding: 40px 0; border-bottom: 1px solid var(--accent); }
header h1 { font-size: 1.8rem; font-weight: 700; }
header h1 span { color: var(--accent); }
header p { color: var(--dim); margin-top: 8px; font-size: 0.9rem; }
nav { background: var(--card); border-bottom: 1px solid var(--border); padding: 12px 0; position: sticky; top: 0; z-index: 100; }
nav .nav-inner { max-width: 800px; margin: 0 auto; padding: 0 20px; display: flex; gap: 16px; align-items: center; flex-wrap: wrap; }
nav a { color: var(--dim); text-decoration: none; padding: 8px 16px; border-radius: 6px; font-size: 0.85rem; white-space: nowrap; transition: all 0.2s; }
nav a:hover, nav a.active { color: var(--accent); background: rgba(16,185,129,0.1); }
.diary-entry { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 32px; margin: 24px 0; transition: border-color 0.2s; }
.diary-entry:hover { border-color: rgba(16,185,129,0.3); }
.diary-entry .date { font-size: 0.8rem; color: var(--accent); font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; }
.diary-entry h2 { font-size: 1.3rem; margin: 8px 0 12px; font-weight: 700; }
.diary-entry .summary { color: var(--dim); font-size: 0.9rem; margin-bottom: 16px; padding-bottom: 16px; border-bottom: 1px solid var(--border); font-style: italic; }
.diary-entry .body { font-size: 0.9rem; line-height: 1.8; }
.diary-entry .body h2 { font-size: 1.1rem; color: var(--accent); margin-top: 20px; margin-bottom: 8px; }
.diary-entry .body h3 { font-size: 0.95rem; color: var(--accent2); margin-top: 16px; margin-bottom: 6px; }
.diary-entry .body ul, .diary-entry .body ol { padding-left: 20px; margin: 8px 0; }
.diary-entry .body li { margin-bottom: 4px; }
.diary-entry .body strong { color: var(--text); }
.diary-entry .body code { background: rgba(16,185,129,0.1); padding: 2px 6px; border-radius: 3px; font-size: 0.85em; }
.diary-entry .tags { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 16px; }
.diary-entry .tag { font-size: 0.7rem; padding: 3px 10px; border-radius: 12px; background: rgba(59,130,246,0.1); color: var(--accent2); border: 1px solid rgba(59,130,246,0.2); }
.diary-entry .toggle-body { cursor: pointer; color: var(--accent); font-size: 0.8rem; margin-top: 12px; display: inline-block; user-select: none; }
.diary-entry .toggle-body:hover { text-decoration: underline; }
.diary-entry .body-content { overflow: hidden; transition: max-height 0.3s ease; }
.diary-entry .body-content.collapsed { max-height: 0; }
.empty-state { text-align: center; padding: 80px 20px; color: var(--dim); }
.empty-state h2 { font-size: 1.2rem; margin-bottom: 8px; }
.stats-row { display: flex; gap: 16px; margin: 24px 0; flex-wrap: wrap; }
.stats-row .stat { background: rgba(16,185,129,0.05); border: 1px solid rgba(16,185,129,0.2); border-radius: 8px; padding: 12px 20px; flex: 1; min-width: 120px; text-align: center; }
.stats-row .stat .num { font-size: 1.5rem; font-weight: 700; color: var(--accent); }
.stats-row .stat .label { font-size: 0.7rem; color: var(--dim); text-transform: uppercase; letter-spacing: 0.05em; margin-top: 2px; }
.archive-list { margin: 24px 0; }
.archive-list h3 { font-size: 1rem; color: var(--accent); margin-bottom: 12px; }
.archive-list ul { list-style: none; display: flex; gap: 8px; flex-wrap: wrap; }
.archive-list a { display: inline-block; padding: 6px 14px; background: var(--card); border: 1px solid var(--border); border-radius: 6px; color: var(--dim); text-decoration: none; font-size: 0.85rem; transition: all 0.2s; }
.archive-list a:hover { color: var(--accent); border-color: var(--accent); }
.archive-list a.current { color: var(--accent); border-color: var(--accent); background: rgba(16,185,129,0.1); }
.archive-list .count { font-size: 0.7rem; color: var(--dim); margin-left: 4px; }
footer { padding: 40px 0; text-align: center; color: var(--dim); font-size: 0.8rem; }
@media (max-width: 768px) { .container { padding: 0 16px; } .diary-entry { padding: 20px; } }"""

JS = """\
function toggleBody(i) {
  var el = document.getElementById('body-' + i);
  var btn = document.getElementById('toggle-' + i);
  if (el.classList.contains('collapsed')) {
    el.classList.remove('collapsed');
    el.style.maxHeight = el.scrollHeight + 'px';
    btn.textContent = '折りたたむ';
  } else {
    el.style.maxHeight = '0';
    el.classList.add('collapsed');
    btn.textContent = '詳細を表示';
  }
}"""

WEEKDAYS = ['月', '火', '水', '木', '金', '土', '日']


def load_entries():
    entries = []
    if not os.path.isfile(ENTRIES_PATH):
        return entries
    with open(ENTRIES_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    entries.reverse()
    return entries


def parse_ts(ts):
    try:
        return datetime.fromisoformat(ts.replace('Z', '+00:00'))
    except Exception:
        return None


def entry_month_key(entry):
    dt = parse_ts(entry.get('ts', ''))
    return f'{dt.year}-{dt.month:02d}' if dt else 'unknown'


def format_date(ts):
    dt = parse_ts(ts)
    if not dt:
        return ts
    wd = WEEKDAYS[dt.weekday()]
    return f'{dt.year}年{dt.month}月{dt.day}日({wd}) {dt.hour:02d}:{dt.minute:02d} UTC'


def month_label(key):
    try:
        y, m = key.split('-')
        return f'{y}年{int(m)}月'
    except Exception:
        return key


def md_to_html(text):
    if not text:
        return ''
    t = html.escape(text)
    t = re.sub(r'^### (.+)$', r'<h3>\1</h3>', t, flags=re.MULTILINE)
    t = re.sub(r'^## (.+)$', r'<h2>\1</h2>', t, flags=re.MULTILINE)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
    t = re.sub(r'^- (.+)$', r'<li>\1</li>', t, flags=re.MULTILINE)
    t = re.sub(r'((?:<li>.*?</li>\n?)+)', r'<ul>\1</ul>', t)
    t = re.sub(r'\n\n', '<br><br>', t)
    t = re.sub(r'\n(?!<)', '<br>', t)
    return t


def build_entry_html(entry, index, expand_first=True):
    date_str = format_date(entry.get('ts', ''))
    title = html.escape(entry.get('title', 'Progress Report'))
    summary = html.escape(entry.get('summary', ''))
    body_html = md_to_html(entry.get('body', ''))
    tags = entry.get('tags', [])
    is_first = expand_first and index == 0
    collapsed_class = '' if is_first else ' collapsed'
    toggle_text = '折りたたむ' if is_first else '詳細を表示'

    tags_html = ''
    if tags:
        tag_spans = ''.join(f'<span class="tag">{html.escape(t)}</span>' for t in tags)
        tags_html = f'<div class="tags">{tag_spans}</div>'

    return f'''
      <article class="diary-entry">
        <div class="date">{date_str}</div>
        <h2>{title}</h2>
        <div class="summary">{summary}</div>
        <div class="body-content{collapsed_class}" id="body-{index}">
          <div class="body">{body_html}</div>
        </div>
        <span class="toggle-body" onclick="toggleBody({index})" id="toggle-{index}">{toggle_text}</span>
        {tags_html}
      </article>'''


def build_archive_links(months_with_counts, current_month=None, path_prefix=''):
    if not months_with_counts:
        return ''
    links = []
    for key, count in months_with_counts:
        cls = ' class="current"' if key == current_month else ''
        href = f'{path_prefix}diary/{key}.html'
        links.append(f'<li><a href="{href}"{cls}>{month_label(key)}<span class="count">({count})</span></a></li>')
    return f'''
  <div class="archive-list">
    <h3>Archive</h3>
    <ul>{"".join(links)}</ul>
  </div>'''


def build_page(title, subtitle, nav_diary_active, entries_html, stats_html,
               archive_html, path_prefix=''):
    return f'''<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — BioEco Agent Lab</title>
<style>
{CSS}
</style>
</head>
<body>

<header>
<div class="container">
  <h1><span>Research</span> Diary</h1>
  <p>{html.escape(subtitle)}</p>
</div>
</header>

<nav>
<div class="nav-inner">
  <a href="{path_prefix}index.html">Portal</a>
  <a href="{path_prefix}publications.html">Publications</a>
  <a href="{path_prefix}diary.html"{"" if not nav_diary_active else ' class="active"'}>Diary</a>
</div>
</nav>

<div class="container">
  <div class="stats-row">
      {stats_html}
  </div>
{archive_html}
  <div id="diary-entries">
{entries_html}
  </div>
</div>

<footer>
<p>BioEco Agent Lab — Research Diary updated every 12 hours by Jim Leader</p>
</footer>

<script>
{JS}
</script>
</body>
</html>'''


def build_stats_html(entries, label_prefix=''):
    total = len(entries)
    if total == 0:
        return ''
    tags = {}
    for e in entries:
        for t in e.get('tags', []):
            tags[t] = tags.get(t, 0) + 1
    top_tags = sorted(tags.items(), key=lambda x: -x[1])[:3]
    latest_dt = parse_ts(entries[0]['ts'])
    latest_str = f'{latest_dt.month}/{latest_dt.day}' if latest_dt else '-'

    parts = [
        f'<div class="stat"><div class="num">{total}</div><div class="label">{label_prefix}Entries</div></div>',
        f'<div class="stat"><div class="num">{latest_str}</div><div class="label">Latest</div></div>',
    ]
    for tag, count in top_tags:
        parts.append(f'<div class="stat"><div class="num">{count}</div><div class="label">{html.escape(tag)}</div></div>')
    return '\n      '.join(parts)


def generate():
    entries = load_entries()

    # Group by month
    by_month = defaultdict(list)
    for e in entries:
        by_month[entry_month_key(e)].append(e)
    months_sorted = sorted(by_month.keys(), reverse=True)
    months_with_counts = [(m, len(by_month[m])) for m in months_sorted]

    # === diary.html (latest 20) ===
    recent = entries[:MAX_RECENT]
    if recent:
        entries_html = '\n'.join(build_entry_html(e, i) for i, e in enumerate(recent))
        if len(entries) > MAX_RECENT:
            entries_html += f'\n      <p style="text-align:center;color:var(--dim);margin:32px 0;font-size:0.9rem">Showing latest {MAX_RECENT} of {len(entries)} entries. See archive for older entries.</p>'
    else:
        entries_html = '''
      <div class="empty-state">
        <h2>No diary entries yet</h2>
        <p>Jim Leader writes progress reports every 12 hours.</p>
      </div>'''

    stats_html = build_stats_html(entries)
    archive_html = build_archive_links(months_with_counts, path_prefix='')

    page = build_page(
        title='Research Diary',
        subtitle="BioEco Agent Lab — Jim Leader's 12-hour progress reports",
        nav_diary_active=True,
        entries_html=entries_html,
        stats_html=stats_html,
        archive_html=archive_html,
        path_prefix='',
    )
    output_path = os.path.join(SITE_DIR, 'diary.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(page)
    print(f'Generated diary.html ({len(recent)} entries)')

    # === Monthly archive pages ===
    for month_key in months_sorted:
        month_entries = by_month[month_key]
        m_entries_html = '\n'.join(build_entry_html(e, i, expand_first=True)
                                   for i, e in enumerate(month_entries))
        m_stats_html = build_stats_html(month_entries, label_prefix=f'{month_label(month_key)} ')
        m_archive_html = build_archive_links(months_with_counts, current_month=month_key, path_prefix='')

        m_page = build_page(
            title=f'Research Diary — {month_label(month_key)}',
            subtitle=f'BioEco Agent Lab — {month_label(month_key)}の研究日報',
            nav_diary_active=False,
            entries_html=m_entries_html,
            stats_html=m_stats_html,
            archive_html=m_archive_html,
            path_prefix='../',
        )
        m_output = os.path.join(SCRIPT_DIR, f'{month_key}.html')
        with open(m_output, 'w', encoding='utf-8') as f:
            f.write(m_page)
        print(f'Generated diary/{month_key}.html ({len(month_entries)} entries)')


if __name__ == '__main__':
    generate()
