import markdown, os, re, json

ROOT = r"C:\Users\ityshchenko\OneDrive - Microsoft\Documents\Microsoft Scout\claude-architect-exam-study-guide"
HTML_OUT = os.path.join(ROOT, "_pdf_build_html")
os.makedirs(HTML_OUT, exist_ok=True)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {{
    --navy: #1B2A6B;
    --orange: #E87A2D;
    --peach: #FFE8E0;
    --slate: #24304F;
    --muted: #5B6475;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: 'Manrope', Arial, sans-serif;
    color: var(--slate);
    margin: 0;
    padding: 36px 48px 56px 48px;
    font-size: 11.5pt;
    line-height: 1.5;
  }}
  .eyebrow {{
    display: inline-block;
    background: var(--peach);
    color: var(--navy);
    font-weight: 700;
    font-size: 10pt;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    padding: 5px 14px;
    border-radius: 999px;
    margin-bottom: 14px;
  }}
  h1 {{
    color: var(--navy);
    font-size: 22pt;
    font-weight: 800;
    margin: 0 0 4px 0;
    line-height: 1.25;
  }}
  h1 .accent {{ color: var(--orange); }}
  .subtitle {{
    color: var(--muted);
    font-size: 11pt;
    margin: 0 0 20px 0;
  }}
  blockquote {{
    background: #F7F8FC;
    border-left: 4px solid var(--orange);
    margin: 0 0 18px 0;
    padding: 10px 16px;
    color: var(--slate);
    font-size: 11pt;
    border-radius: 0 6px 6px 0;
  }}
  h2 {{
    color: var(--navy);
    font-size: 15pt;
    font-weight: 800;
    margin: 24px 0 10px 0;
    border-bottom: 2px solid var(--peach);
    padding-bottom: 6px;
  }}
  h3 {{
    color: var(--navy);
    font-size: 12.5pt;
    font-weight: 700;
    margin: 20px 0 6px 0;
    page-break-after: avoid;
  }}
  p {{ margin: 6px 0; }}
  ul, ol {{ margin: 6px 0; padding-left: 22px; }}
  li {{ margin: 2px 0; }}
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 18px 0;
    font-size: 10pt;
  }}
  th {{
    background: var(--navy);
    color: #fff;
    text-align: left;
    padding: 6px 8px;
  }}
  td {{
    border-bottom: 1px solid #E5E8F0;
    padding: 6px 8px;
    vertical-align: top;
  }}
  strong {{ color: var(--navy); }}
  a {{ color: var(--orange); text-decoration: none; }}
  hr {{
    border: none;
    border-top: 2px solid var(--peach);
    margin: 20px 0;
  }}
  .question-block {{
    page-break-inside: avoid;
    margin-bottom: 14px;
  }}
  code {{
    background: #F0F1F6;
    padding: 1px 5px;
    border-radius: 4px;
    font-size: 10pt;
  }}
</style>
</head>
<body>
<div class="eyebrow">Claude Certified Architect &mdash; Foundations</div>
{body}
</body>
</html>
"""

HEADER_TEMPLATE = """
<div style="font-size:8px; width:100%; padding:4px 36px 0 36px; color:#5B6475; font-family: Manrope, Arial, sans-serif; display:flex; justify-content:space-between;">
  <span>Claude Certified Architect &ndash; Foundations: Exam Study Guide</span>
  <span>Iryna Tyshchenko</span>
</div>
"""

FOOTER_TEMPLATE = """
<div style="font-size:8px; width:100%; padding:0 36px 6px 36px; color:#ffffff; background:#1B2A6B; font-family: Manrope, Arial, sans-serif; display:flex; justify-content:space-between; align-items:center;">
  <span>in/iryna-tyshchenko &middot; LinkedIn</span>
  <span class="pageNumber"></span>/<span class="totalPages"></span>
</div>
"""


def md_to_html(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    # Extract H1 title for <title> tag and split into accent word (last word colored orange)
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    raw_title = m.group(1).strip() if m else os.path.basename(md_path)
    # strip nav links lines like "[← Back ...]" so they don't clutter the PDF
    text = re.sub(r"^\[.*Back to.*\].*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\[.*Next:.*\].*$", "", text, flags=re.MULTILINE)
    html_body = markdown.markdown(text, extensions=["tables", "fenced_code"])
    return raw_title, html_body


def build(md_path, html_path):
    title, body = md_to_html(md_path)
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    html = TEMPLATE.format(title=title, body=body)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    manifest = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        if "_pdf_build_html" in dirpath or ".git" in dirpath:
            continue
        for fn in filenames:
            if fn.lower().endswith(".md"):
                src = os.path.join(dirpath, fn)
                rel = os.path.relpath(src, ROOT)
                rel_html = os.path.splitext(rel)[0] + ".html"
                rel_pdf = os.path.splitext(rel)[0] + ".pdf"
                html_path = os.path.join(HTML_OUT, rel_html)
                build(src, html_path)
                manifest.append({
                    "html": html_path,
                    "pdf": os.path.join(ROOT, "pdf", rel_pdf),
                })
    with open(os.path.join(ROOT, "_pdf_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"Built {len(manifest)} HTML files. Manifest written.")


if __name__ == "__main__":
    main()
