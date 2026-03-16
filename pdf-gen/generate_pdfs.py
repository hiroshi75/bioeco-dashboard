#!/usr/bin/env python3
"""Generate academic-style PDFs from Markdown files.
Supports English (Helvetica/Times) and Japanese (HeiseiMin/HeiseiKakuGo CID fonts).
"""
import re, os, sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable,
    Table, TableStyle
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# Register Japanese CID fonts
for font_name in ['HeiseiMin-W3', 'HeiseiKakuGo-W5']:
    try:
        pdfmetrics.registerFont(UnicodeCIDFont(font_name))
    except Exception:
        pass


def make_styles(is_japanese=False):
    """Create paragraph styles for English or Japanese."""
    styles = getSampleStyleSheet()

    body_font = 'HeiseiMin-W3' if is_japanese else 'Times-Roman'
    heading_font = 'HeiseiKakuGo-W5' if is_japanese else 'Helvetica-Bold'
    heading_font_bi = 'HeiseiKakuGo-W5' if is_japanese else 'Helvetica-BoldOblique'

    custom = {}
    custom['PaperTitle'] = ParagraphStyle(
        'PaperTitle', parent=styles['Title'],
        fontName=heading_font, fontSize=15, leading=20, spaceAfter=4,
        textColor=HexColor('#1a1a2e'), alignment=TA_LEFT
    )
    custom['Meta'] = ParagraphStyle(
        'Meta', parent=styles['Normal'],
        fontName=body_font, fontSize=8, leading=11,
        textColor=HexColor('#888888'), spaceAfter=14
    )
    custom['H1'] = ParagraphStyle(
        'H1x', parent=styles['Heading1'],
        fontName=heading_font, fontSize=13, leading=17,
        spaceBefore=16, spaceAfter=6, textColor=HexColor('#1a1a2e')
    )
    custom['H2'] = ParagraphStyle(
        'H2x', parent=styles['Heading2'],
        fontName=heading_font, fontSize=11, leading=14,
        spaceBefore=12, spaceAfter=5, textColor=HexColor('#2d3748')
    )
    custom['H3'] = ParagraphStyle(
        'H3x', parent=styles['Heading3'],
        fontName=heading_font_bi, fontSize=10, leading=13,
        spaceBefore=8, spaceAfter=3, textColor=HexColor('#4a5568')
    )
    custom['Body'] = ParagraphStyle(
        'Bodyx', parent=styles['Normal'],
        fontName=body_font, fontSize=9.5, leading=13.5,
        spaceAfter=5, alignment=TA_JUSTIFY
    )
    custom['BulletItem'] = ParagraphStyle(
        'BulletItem', parent=styles['Normal'],
        fontName=body_font, fontSize=9, leading=12.5,
        spaceAfter=2, leftIndent=16
    )
    custom['Cell'] = ParagraphStyle(
        'Cellx', parent=styles['Normal'],
        fontName=body_font, fontSize=7.5, leading=10
    )
    custom['CellHead'] = ParagraphStyle(
        'CellHead', parent=styles['Normal'],
        fontName=heading_font, fontSize=7.5, leading=10
    )
    return custom


def clean_md(text):
    """Strip markdown formatting to plain text safe for reportlab Paragraph."""
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    t = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<i>\1</i>', t)
    t = re.sub(r'`(.+?)`', r'\1', t)
    t = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', t)
    # Protect our tags, escape XML
    tags = []
    def save_tag(m):
        tags.append(m.group(0))
        return f'\x00TAG{len(tags)-1}\x00'
    t = re.sub(r'</?[bi]>', save_tag, t)
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    for i, tag in enumerate(tags):
        t = t.replace(f'\x00TAG{i}\x00', tag)
    return t.strip()


def flush_table(story, rows, styles):
    if not rows:
        return
    ncols = max(len(r) for r in rows)
    for r in rows:
        while len(r) < ncols:
            r.append('')
    data = []
    for i, row in enumerate(rows):
        st = styles['CellHead'] if i == 0 else styles['Cell']
        data.append([Paragraph(clean_md(c), st) for c in row])
    w = 160 * mm / ncols if ncols else 160 * mm
    tbl = Table(data, colWidths=[w] * ncols)
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#edf2f7')),
        ('GRID', (0, 0), (-1, -1), 0.4, HexColor('#cbd5e0')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 3),
        ('RIGHTPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(Spacer(1, 4))
    story.append(tbl)
    story.append(Spacer(1, 4))


def md_to_pdf(md_path, pdf_path, is_japanese=False):
    with open(md_path, encoding='utf-8') as f:
        lines = f.readlines()

    styles = make_styles(is_japanese)
    story = []
    table_buf = []
    in_table = False
    title_done = False

    for raw in lines:
        line = raw.rstrip()

        # Table handling
        if line.startswith('|'):
            if re.match(r'^\|[\s\-:|]+\|$', line):
                continue  # separator row
            cells = [c.strip() for c in line.split('|')[1:-1]]
            table_buf.append(cells)
            in_table = True
            continue
        elif in_table:
            flush_table(story, table_buf, styles)
            table_buf = []
            in_table = False

        if not line or line == '---':
            if line == '---':
                story.append(HRFlowable(width="100%", thickness=0.4,
                             color=HexColor('#d0d0d0'), spaceAfter=6, spaceBefore=6))
            else:
                story.append(Spacer(1, 3))
            continue

        if line.startswith('# ') and not title_done:
            title_done = True
            story.append(Paragraph(clean_md(line[2:]), styles['PaperTitle']))
            lang = '日本語版' if is_japanese else 'English'
            story.append(Paragraph(f'BioEco Agent Lab | Draft Manuscript ({lang})', styles['Meta']))
            continue

        if line.startswith('# '):
            story.append(Paragraph(clean_md(line[2:]), styles['H1']))
        elif line.startswith('## '):
            story.append(Paragraph(clean_md(line[3:]), styles['H2']))
        elif line.startswith('### '):
            story.append(Paragraph(clean_md(line[4:]), styles['H3']))
        elif line.startswith('- ') or line.startswith('* '):
            story.append(Paragraph('\u2022 ' + clean_md(line[2:]), styles['BulletItem']))
        else:
            txt = clean_md(line)
            if txt:
                try:
                    story.append(Paragraph(txt, styles['Body']))
                except Exception:
                    # Skip problematic lines
                    pass

    # flush remaining table
    if table_buf:
        flush_table(story, table_buf, styles)

    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=25*mm, rightMargin=25*mm,
                            topMargin=20*mm, bottomMargin=20*mm)
    doc.build(story)
    kb = os.path.getsize(pdf_path) // 1024
    tag = 'JA' if is_japanese else 'EN'
    print(f"  [{tag}] {os.path.basename(pdf_path)} ({kb}KB)")


def main():
    BASE = os.path.expanduser(
        '~/.agentlattice/bioeco/agents/jim-leader/workspace')
    SRC = f'{BASE}/website/pdf-source'
    DST = f'{BASE}/final-result'

    jobs = [
        # English
        (f'{SRC}/paper5-full.md',
         f'{DST}/20260317120000-paper5-ghost-signals/manuscript/paper5-ghost-signals-manuscript.pdf', False),
        (f'{SRC}/paper1-full.md',
         f'{DST}/20260317120100-paper1-apparent-stability/manuscript/paper1-apparent-stability-manuscript.pdf', False),
        (f'{SRC}/grl-note-full.md',
         f'{DST}/20260317120200-grl-note-mhw-sanriku/manuscript/grl-note-mhw-sanriku-manuscript.pdf', False),
        (f'{SRC}/sti-note-full.md',
         f'{DST}/20260317120300-sti-methods-note/manuscript/sti-methods-note-manuscript.pdf', False),
        # Japanese
        (f'{SRC}/paper5-full-ja.md',
         f'{DST}/20260317120000-paper5-ghost-signals/manuscript/paper5-ghost-signals-manuscript-ja.pdf', True),
        (f'{SRC}/paper1-full-ja.md',
         f'{DST}/20260317120100-paper1-apparent-stability/manuscript/paper1-apparent-stability-manuscript-ja.pdf', True),
        (f'{SRC}/grl-note-full-ja.md',
         f'{DST}/20260317120200-grl-note-mhw-sanriku/manuscript/grl-note-mhw-sanriku-manuscript-ja.pdf', True),
        (f'{SRC}/sti-note-full-ja.md',
         f'{DST}/20260317120300-sti-methods-note/manuscript/sti-methods-note-manuscript-ja.pdf', True),
        # Working Papers
        (f'{SRC}/rdd-working-paper.md',
         f'{DST}/20260317120400-rdd-protected-areas/manuscript/rdd-working-paper.pdf', False),
        (f'{SRC}/seasonal-divergence-working-paper.md',
         f'{DST}/20260317120500-seasonal-divergence/manuscript/seasonal-divergence-working-paper.pdf', False),
    ]

    print('Generating PDFs...')
    for src, dst, ja in jobs:
        if not os.path.isfile(src):
            print(f'  SKIP {os.path.basename(src)} (not found)')
            continue
        try:
            md_to_pdf(src, dst, is_japanese=ja)
        except Exception as e:
            print(f'  ERROR {os.path.basename(src)}: {e}')

    print('Done!')


if __name__ == '__main__':
    main()
