#!/usr/bin/env python3
"""Génère le site statique à partir de content/ vers docs/."""

import json
import re
import shutil
from pathlib import Path
from typing import Optional

import markdown
from markdown.extensions.tables import TableExtension

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
DOCS = ROOT / "docs"
ASSETS_SRC = ROOT / "assets"
NAV_FILE = ROOT / "navigation.json"


def collect_pages():
    pages = {}
    for md_file in sorted(CONTENT.rglob("*.md")):
        rel = md_file.relative_to(CONTENT)
        key = str(rel.with_suffix("")).replace("\\", "/")
        pages[key] = md_file
    return pages


def resolve_wikilink(link: str, current_key: str, pages: dict) -> Optional[str]:
    """Résout un lien Obsidian vers une clé de page publiée, ou None."""
    link = link.strip()
    if "|" in link:
        link = link.split("|", 1)[0].strip()

  # Chemin relatif explicite
    if "/" in link or link.startswith(".."):
        current_dir = Path(current_key).parent
        target = (current_dir / link).as_posix()
        # Normaliser ..
        parts = []
        for part in target.split("/"):
            if part == "..":
                if parts:
                    parts.pop()
            elif part and part != ".":
                parts.append(part)
        target = "/".join(parts)
    else:
        current_dir = Path(current_key).parent
        target = (current_dir / link).as_posix()

    # Essayer avec et sans extension implicite
    candidates = [target, target.replace("Cours - ", "")]
    for cand in candidates:
        if cand in pages:
            return cand
        # Recherche par nom de fichier seul
        for key in pages:
            if key.endswith("/" + cand) or key == cand:
                return key
            if Path(key).name == cand or Path(key).name == cand + ".md":
                return key
    return None


def wikilink_to_html(match, current_key: str, pages: dict) -> str:
    raw = match.group(1)
    display = raw.split("|", 1)[1].strip() if "|" in raw else raw.split("/")[-1]
    target_key = resolve_wikilink(raw, current_key, pages)
    if target_key:
        href = relative_html_path(current_key, target_key)
        return f'<a href="{href}">{display}</a>'
    return f'<span class="link-unpublished" title="Page non publiée">{display}</span>'


def html_path_for(key: str) -> str:
    depth = key.count("/")
    prefix = "../" * (depth + 1) if depth >= 0 else ""
    # Depuis docs/01 - Virtualisation/file.html -> ../ pour index, ./ pour sibling
    parts = key.split("/")
    if len(parts) == 1:
        return f"./{parts[0]}.html"
    return "/".join(parts[:-1]) + "/" + parts[-1] + ".html"


def relative_html_path(from_key: str, to_key: str) -> str:
    from_parts = from_key.split("/")
    to_parts = to_key.split("/")
    # Répertoire source
    from_dir = from_parts[:-1]
    to_file = "/".join(to_parts) + ".html"
    # Remonter
    ups = len(from_dir)
    prefix = "../" * ups if ups else "./"
    if not from_dir:
        return to_file
    return prefix + to_file


pages_global = {}


def convert_obsidian_embeds(text: str) -> str:
    def repl(m):
        raw = m.group(1).strip()
        if "|" in raw:
            path, alt = raw.split("|", 1)
            return f"![{alt.strip()}]({path.strip()})"
        return f"![]({raw})"
    return re.sub(r"!\[\[([^\]]+)\]\]", repl, text)


def convert_wikilinks(text: str, current_key: str) -> str:
    def repl(m):
        return wikilink_to_html(m, current_key, pages_global)
    return re.sub(r"(?<!!)\[\[([^\]]+)\]\]", repl, text)


IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}


def copy_content_assets():
    for src in CONTENT.rglob("*"):
        if src.is_file() and src.suffix.lower() in IMAGE_EXTS:
            rel = src.relative_to(CONTENT)
            dest = DOCS / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(src), str(dest))


def build_navigation(pages: dict) -> list:
    nav = []
    for key in sorted(pages.keys()):
        title = Path(key).stem
        nav.append({"path": key, "title": title, "html": html_path_for(key)})
    return nav


def page_template(title: str, body: str, nav_items: list, current_key: str) -> str:
    nav_html = []
    for item in nav_items:
        href = relative_html_path(current_key, item["path"])
        active = " active" if item["path"] == current_key else ""
        nav_html.append(
            f'<li><a href="{href}" class="nav-link{active}">{item["title"]}</a></li>'
        )
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — AdmSys</title>
  <link rel="stylesheet" href="{relative_html_path(current_key, '__assets__/style.css').replace('__assets__/style.css', '../' * (current_key.count('/') + 1) + 'assets/style.css')}">
</head>
<body>
  <div class="layout">
    <nav class="sidebar">
      <div class="site-title"><a href="{relative_html_path(current_key, 'index')}">AdmSys</a></div>
      <ul class="nav-list">
        {''.join(nav_html)}
      </ul>
    </nav>
    <main class="content">
      <article>{body}</article>
    </main>
  </div>
</body>
</html>"""


def css_href(current_key: str) -> str:
    depth = current_key.count("/") + 1
    return "../" * depth + "assets/style.css"


def page_template_v2(title: str, body: str, nav_items: list, current_key: str) -> str:
    nav_html = []
    for item in nav_items:
        href = relative_html_path(current_key, item["path"])
        active = " active" if item["path"] == current_key else ""
        nav_html.append(
            f'<li><a href="{href}" class="nav-link{active}">{item["title"]}</a></li>'
        )
    index_href = "../" * current_key.count("/") + ("index.html" if current_key.count("/") else "./index.html")
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — AdmSys</title>
  <link rel="stylesheet" href="{css_href(current_key)}">
</head>
<body>
  <div class="layout">
    <nav class="sidebar">
      <div class="site-title"><a href="{index_href}">AdmSys</a></div>
      <ul class="nav-list">
        {''.join(nav_html)}
      </ul>
    </nav>
    <main class="content">
      <article>{body}</article>
    </main>
  </div>
</body>
</html>"""


def index_template(nav_items: list) -> str:
    links = []
    for item in nav_items:
        links.append(f'<li><a href="{item["html"]}">{item["title"]}</a></li>')
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AdmSys — Administration Systèmes</title>
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>
  <div class="layout">
    <nav class="sidebar">
      <div class="site-title"><a href="index.html">AdmSys</a></div>
      <ul class="nav-list">
        {''.join(f'<li><a href="{item["html"]}" class="nav-link">{item["title"]}</a></li>' for item in nav_items)}
      </ul>
    </nav>
    <main class="content">
      <h1>Administration Systèmes</h1>
      <p>Documentation publique du parcours AdmSys.</p>
      <h2>Cours publiés</h2>
      <ul>
        {''.join(links)}
      </ul>
    </main>
  </div>
</body>
</html>"""


def check_links(pages: dict) -> list:
    issues = []
    wikilink_re = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")
    for key, md_file in pages.items():
        text = md_file.read_text(encoding="utf-8")
        for m in wikilink_re.finditer(text):
            raw = m.group(1)
            if resolve_wikilink(raw, key, pages) is None:
                display = raw.split("|")[-1].strip()
                issues.append({"file": key, "link": raw, "display": display})
        for img in re.findall(r"!\[\[([^\]]+)\]\]", text):
            img = img.split("|", 1)[0].strip()
            img_path = (md_file.parent / img).resolve()
            if not img_path.exists():
                issues.append({"file": key, "type": "image", "link": img})
        for img in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
            img_path = (md_file.parent / img).resolve()
            if not img_path.exists():
                issues.append({"file": key, "type": "image", "link": img})
    return issues


def main():
    global pages_global
    pages = collect_pages()
    pages_global = pages

    if not DOCS.exists():
        DOCS.mkdir()

    nav = build_navigation(pages)
    NAV_FILE.write_text(json.dumps(nav, indent=2, ensure_ascii=False), encoding="utf-8")

    md_ext = markdown.Markdown(extensions=[TableExtension(), "fenced_code"])
    (DOCS / "assets").mkdir(parents=True, exist_ok=True)
    for item in ASSETS_SRC.iterdir():
        dest = DOCS / "assets" / item.name
        if item.is_dir():
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(str(item), str(dest))
        else:
            shutil.copy2(str(item), str(dest))

    copy_content_assets()

    for key, md_file in pages.items():
        text = md_file.read_text(encoding="utf-8")
        text = convert_obsidian_embeds(text)
        text = convert_wikilinks(text, key)
        md_ext.reset()
        body = md_ext.convert(text)
        title = Path(key).stem
        html = page_template_v2(title, body, nav, key)
        out = DOCS / (key + ".html")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")

    (DOCS / "index.html").write_text(index_template(nav), encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    issues = check_links(pages)
    if issues:
        print("AVERTISSEMENTS — liens non publiés ou ressources manquantes :")
        for issue in issues:
            if issue.get("type") == "image":
                print(f"  [{issue['file']}] image manquante : {issue['link']}")
            else:
                print(f"  [{issue['file']}] lien non publié : [[{issue['link']}]]")
    print(f"Site généré : {len(pages)} page(s) dans {DOCS}")


if __name__ == "__main__":
    main()
