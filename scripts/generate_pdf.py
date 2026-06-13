from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Preformatted, Spacer, PageBreak
from reportlab.lib.units import mm


TEXT_EXTS = {
    '.py', '.md', '.txt', '.csv', '.json', '.yml', '.yaml', '.html', '.htm',
    '.css', '.js', '.rst', '.ini', '.cfg', '.toml', '.log', '.sql'
}


def is_text_file(path: Path) -> bool:
    if path.suffix.lower() in TEXT_EXTS:
        return True
    # quick sniff: try open and decode
    try:
        with path.open('rb') as fh:
            chunk = fh.read(2048)
            if not chunk:
                return True
            chunk.decode('utf-8')
            return True
    except Exception:
        return False


def gather_files(root: Path):
    files = []
    for p in sorted(root.rglob('*')):
        if not p.is_file():
            continue
        parts = {s.lower() for s in p.parts}
        if '.git' in parts or 'venv' in parts or '__pycache__' in parts:
            continue
        # skip large binaries
        try:
            size = p.stat().st_size
        except Exception:
            size = 0
        if p.suffix.lower() not in TEXT_EXTS and size > 5_000_000:
            continue
        files.append(p)
    return files


def make_pdf(root: Path, out_path: Path):
    doc = SimpleDocTemplate(str(out_path), pagesize=A4,
                            rightMargin=15*mm, leftMargin=15*mm,
                            topMargin=15*mm, bottomMargin=15*mm)
    styles = getSampleStyleSheet()
    title_style = styles['Heading2']
    code_style = ParagraphStyle('Code', parent=styles.get('Code', styles['Normal']), fontName='Courier', fontSize=8, leading=9)

    flow = []

    files = gather_files(root)
    if not files:
        flow.append(Paragraph('No files found', title_style))

    for idx, f in enumerate(files, 1):
        rel = f.relative_to(root)
        flow.append(Paragraph(f'{idx}. {rel}', title_style))
        flow.append(Spacer(1, 4))
        if is_text_file(f):
            try:
                text = f.read_text(encoding='utf-8', errors='replace')
            except Exception:
                text = f.read_text(encoding='latin-1', errors='replace')
            flow.append(Preformatted(text, code_style))
        else:
            flow.append(Paragraph('Binary or non-text file — skipped', styles['Normal']))
        flow.append(PageBreak())

    doc.build(flow)


def main():
    root = Path(__file__).resolve().parents[1]
    out = root / 'all_files_combined.pdf'
    print('Scanning', root)
    make_pdf(root, out)
    print('Wrote', out)


if __name__ == '__main__':
    main()
