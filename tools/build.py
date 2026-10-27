#!/usr/bin/env python3
"""Generate the static pages for andrewtechsolutions.cloud in every language.

usage: python3 tools/build.py <site root> <folder containing the app repos>
English is served at /, other languages at /<code>/ (see tools/i18n.py).
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from i18n import LANGS, T

ROOT = sys.argv[1]
SRC = sys.argv[2]
MAIL = "dodangtruong2002@gmail.com"
HOST = "https://andrewtechsolutions.cloud"
PLAY_CHESS = "https://play.google.com/store/apps/details?id=com.andrewtechsolutions.boardgames"
PLAY_TAROT = "https://play.google.com/store/apps/details?id=com.victor.tarot"

ICON_PLAY = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3.6 2.3 13.3 12l-9.7 9.7c-.4-.3-.6-.8-.6-1.4V3.7c0-.6.2-1.1.6-1.4zm1.3-.7c.3 0 .7.1 1 .3l11.4 6.5-2.6 2.6L4.9 1.6zm12.7 7.3 3.3 1.9c1 .6 1 1.9 0 2.5l-3.3 1.9-2.9-2.9 2.9-3.4zM5.9 22.1c-.3.2-.7.3-1 .3l9.8-9.4 2.6 2.6L5.9 22.1z"/></svg>'
ICON_APPLE = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.4 12.6c0-2.5 2-3.7 2.1-3.8-1.2-1.7-3-1.9-3.6-2-1.5-.2-3 .9-3.8.9s-2-.9-3.3-.9C6.1 6.9 4.5 7.9 3.6 9.4c-1.9 3.3-.5 8.1 1.3 10.8.9 1.3 2 2.7 3.4 2.7 1.4-.1 1.9-.9 3.5-.9s2.1.9 3.5.9 2.4-1.3 3.3-2.6c1-1.5 1.5-3 1.5-3.1-.1 0-2.9-1.1-2.9-4.6zM14 5.2c.7-.9 1.2-2.1 1.1-3.2-1 0-2.3.7-3 1.6-.7.8-1.3 2-1.1 3.2 1.1.1 2.3-.6 3-1.6z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m8.5 12 2.3 2.3L15.5 9.6"/></svg>'
GLOBE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>'

GAMES = ["Chess", "Chess960", "Xiangqi", "Jieqi", "Go", "Shogi", "Janggi", "Gomoku", "Othello", "Checkers",
         "Connect Four", "Ô Ăn Quan", "Cờ Gánh", "Ludo"]

# Pages that exist in every language, keyed by a logical path. Per-app policies are English only.
PAGES = ["/", "/support/", "/privacy/", "/terms/"]


def write(rel, html):
    p = os.path.join(ROOT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(html)


def head(lang, prefix, t, title, desc, page):
    """page is the logical path ('/', '/support/', ...) used for hreflang alternates."""
    url = f"{HOST}{prefix}{page}"
    alts = "".join(f'<link rel="alternate" hreflang="{c}" href="{HOST}{p}{page}">' for c, _, p in LANGS)
    alts += f'<link rel="alternate" hreflang="x-default" href="{HOST}{page}">'
    n = t["nav"]
    switch = "".join(
        f'<a href="{p}{page}" lang="{c}"{" class=cur" if c == lang else ""}>{name}</a>' for c, name, p in LANGS)
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{HOST}/assets/chess-master.png">
<meta name="theme-color" content="#060a13">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="canonical" href="{url}">
{alts}
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="{prefix}/"><i></i>Andrew Tech Solutions</a>
<nav>
<a href="{prefix}/#apps">{n["apps"]}</a><a href="{prefix}/#why">{n["why"]}</a><a href="{prefix}/support/">{n["support"]}</a><a href="{prefix}/privacy/">{n["privacy"]}</a><a href="{prefix}/terms/">{n["terms"]}</a>
<div class="lang"><button type="button" aria-label="{t["foot"]["lang"]}" aria-haspopup="true">{GLOBE}<span>{lang.upper()}</span></button><div class="menu">{switch}</div></div>
<a class="btn sm" href="{prefix}/#apps">{n["get"]}</a>
</nav>
</div></header>
<main>
'''


def foot(lang, prefix, t, page):
    f = t["foot"]
    switch = "".join(
        f'<a href="{p}{page}" lang="{c}"{" class=cur" if c == lang else ""}>{name}</a>' for c, name, p in LANGS)
    return f'''</main>
<footer class="site"><div class="wrap">
<div class="fgrid">
<div><a class="brand" href="{prefix}/"><i></i>Andrew Tech Solutions</a><p>{f["tag"]}</p></div>
<div><h4>{f["apps"]}</h4><ul><li><a href="{prefix}/#chess">Chess Master</a></li><li><a href="{prefix}/#tarot">Daily Tarot</a></li></ul></div>
<div><h4>{f["legal"]}</h4><ul><li><a href="{prefix}/privacy/">{t["privacy"]["title"]}</a></li><li><a href="{prefix}/terms/">{t["terms"]["title"]}</a></li><li><a href="/app-ads.txt">app-ads.txt</a></li></ul></div>
<div><h4>{f["help"]}</h4><ul><li><a href="{prefix}/support/">{f["faq"]}</a></li><li><a href="mailto:{MAIL}">{f["email"]}</a></li></ul></div>
</div>
<div class="flang"><span>{f["lang"]}</span>{switch}</div>
<div class="fbot"><span>{f["copy"]}</span><span>{f["made"]}</span></div>
</div></footer>
<script>
(function(){{var els=document.querySelectorAll('.rv');if(!('IntersectionObserver' in window)){{els.forEach(function(e){{e.classList.add('in')}})}}else{{
var io=new IntersectionObserver(function(en){{en.forEach(function(x){{if(x.isIntersecting){{x.target.classList.add('in');io.unobserve(x.target)}}}})}},{{threshold:.12}});
els.forEach(function(e){{io.observe(e)}})}}
var l=document.querySelector('.lang');if(l){{var b=l.querySelector('button');b.addEventListener('click',function(e){{e.stopPropagation();l.classList.toggle('open')}});
document.addEventListener('click',function(){{l.classList.remove('open')}})}}}})();
</script>
</body>
</html>
'''


def side(prefix, t):
    s = t["support"]
    return f'''<aside class="side">
<div class="card contact"><h3>{s["side_contact"]}</h3><p>{s["side_reply"]}</p><a class="mail" href="mailto:{MAIL}">{MAIL}</a></div>
<div class="card"><h3>{s["side_apps"]}</h3><ul class="list">
<li><a href="{prefix}/#chess"><img src="/assets/chess-master.png" alt="">Chess Master</a></li>
<li><a href="{prefix}/#tarot"><img src="/assets/daily-tarot.png" alt="">Daily Tarot</a></li></ul></div>
<div class="card"><h3>{s["side_legal"]}</h3><ul class="list"><li><a href="{prefix}/privacy/">{t["privacy"]["title"]}</a></li><li><a href="{prefix}/terms/">{t["terms"]["title"]}</a></li></ul></div>
</aside>'''


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"<[^>]+>", "", s).lower()).strip("-") or "s"


# ---------------- chess board (shared) ----------------
rows = ["rnbqkbnr", "pppppppp", "........", "........", "........", ".....N..", "PPPPP.PP", "RNBQKB.R"]
glyph = {"k": "&#9818;", "q": "&#9819;", "r": "&#9820;", "b": "&#9821;", "n": "&#9822;", "p": "&#9823;",
         "K": "&#9812;", "Q": "&#9813;", "R": "&#9814;", "B": "&#9815;", "N": "&#9816;", "P": "&#9817;"}
cells = []
for r, row in enumerate(rows):
    for c, ch in enumerate(row):
        cls = []
        if ch.isupper(): cls.append("w")
        if (r, c) in [(5, 5), (7, 6)]: cls.append("hl")
        if (r, c) in [(3, 4), (3, 6), (4, 3), (4, 7)]: cls.append("dot")
        cells.append(f'<span class="{" ".join(cls)}">{glyph.get(ch, "")}</span>')
BOARD = "".join(cells)


def build_index(lang, prefix, t):
    h, a, c, ta, w, b = t["hero"], t["apps"], t["chess"], t["tarot"], t["why"], t["band"]
    marquee = "".join(f"<li>{re.sub(r'\s*<small>.*?</small>', '', g)}</li>" for g in t["games"] + t["marquee"])
    feats = lambda fs: "".join(f'<li>{CHECK}<span><b>{x}</b> {y}</span></li>' for x, y in fs)
    icons = [
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4 7v5c0 5 3.4 8.4 8 9 4.6-.6 8-4 8-9V7l-8-4z"/><path d="m9 12 2 2 4-4"/></svg>',
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5 2 10a15 15 0 0 1 20 0l-3 2.5"/><path d="M8.5 16 7 14.6a8 8 0 0 1 10 0L15.5 16"/><circle cx="12" cy="19" r="1.2"/><path d="m3 3 18 18"/></svg>',
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h7l-1 8 9-12h-7l1-8z"/></svg>',
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-4.6-7-11a7 7 0 0 1 14 0c0 6.4-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    ]
    tiles = "".join(f'<div class="tile rv d{i}"><div class="ic">{icons[i]}</div><h3>{x}</h3><p>{y}</p></div>' for i, (x, y) in enumerate(w["t"]))
    return head(lang, prefix, t, "Andrew Tech Solutions", t["site_desc"], "/") + f'''
<div class="wrap"><section class="hero">
<div>
<span class="eyebrow">{h["eyebrow"]}</span>
<h1>{h["h1a"]}<span class="grad">{h["h1b"]}</span></h1>
<p class="lead">{h["lead"]}</p>
<div class="cta"><a class="btn" href="#apps">{h["cta1"]}</a><a class="btn ghost" href="{prefix}/support/">{h["cta2"]}</a></div>
<ul class="stats">
<li><b><span>14</span></b>{h["s1"]}</li>
<li><b><span>78</span></b>{h["s2"]}</li>
<li><b><span>100%</span></b>{h["s3"]}</li>
<li><b><span>0</span></b>{h["s4"]}</li>
</ul>
</div>
<div class="phones">
<div class="orb one"></div><div class="orb two"></div>
<div class="phone a"><img src="/assets/shots/tarot-1-home.png" alt="Daily Tarot" width="250" height="536" loading="eager"></div>
<div class="phone b"><img src="/assets/shots/tarot-5-reading.png" alt="Daily Tarot" width="250" height="536"></div>
</div>
</section></div>

<div class="marquee"><ul>{marquee}{marquee}</ul></div>

<section id="apps" class="wrap">
<div class="sec-head rv"><span class="eyebrow">{a["eyebrow"]}</span><h2>{a["h2a"]}<span class="grad">{a["h2b"]}</span></h2><p>{a["p"]}</p></div>

<div id="chess" class="show">
<div class="copy rv">
<img class="icon" src="/assets/chess-master.png" alt="Chess Master" width="76" height="76">
<span class="tag">{c["tag"]}</span>
<h2>{c["name"]}</h2>
<p>{c["p"]}</p>
<div class="games">{"".join(f"<span>{g}</span>" for g in t["games"])}</div>
<ul class="feat">{feats(c["f"])}</ul>
<div class="cta"><a class="btn" href="{PLAY_CHESS}">{ICON_PLAY}{t["play"]}</a><a class="btn ghost soon" href="#">{ICON_APPLE}{t["appstore"]}</a><span class="meta">{c["meta"]}</span></div>
<p style="margin:14px 0 0;font-size:14px"><a href="/privacy/chess-master/">{c["plink"]}</a></p>
</div>
<div class="visual rv d1">
<div class="glow" style="background:var(--gold);opacity:.18"></div>
<div class="board-wrap">
<div class="board">{BOARD}</div>
<div class="hud"><span>Chess &middot; <b>Nf3</b></span><span class="lvl">★ Master</span><span>#<b>1</b></span></div>
</div>
</div>
</div>

<div id="tarot" class="show flip">
<div class="copy rv">
<img class="icon" src="/assets/daily-tarot.png" alt="Daily Tarot" width="76" height="76">
<span class="tag">{ta["tag"]}</span>
<h2>{ta["name"]}</h2>
<p>{ta["p"]}</p>
<ul class="feat">{feats(ta["f"])}</ul>
<div class="cta"><a class="btn" href="{PLAY_TAROT}">{ICON_PLAY}{t["play"]}</a><a class="btn ghost soon" href="#">{ICON_APPLE}{t["appstore"]}</a><span class="meta">{ta["meta"]}</span></div>
<p style="margin:14px 0 0;font-size:14px"><a href="/privacy/daily-tarot/">{ta["plink"]}</a></p>
</div>
<div class="visual rv d1">
<div class="glow" style="background:var(--c2)"></div>
<div class="tarot-visual">
<div class="phone l"><img src="/assets/shots/tarot-3-spread.png" alt="Daily Tarot" width="240" height="515" loading="lazy"></div>
<div class="phone r"><img src="/assets/shots/tarot-2-daily.png" alt="Daily Tarot" width="240" height="515" loading="lazy"></div>
</div>
</div>
</div>
</section>

<section id="why" class="wrap">
<div class="sec-head rv"><span class="eyebrow">{w["eyebrow"]}</span><h2>{w["h2a"]}<span class="grad">{w["h2b"]}</span></h2><p>{w["p"]}</p></div>
<div class="grid4">{tiles}</div>
</section>

<section class="wrap">
<div class="band rv">
<h2>{b["h2"]}</h2>
<p>{b["p"]}</p>
<div class="cta"><a class="btn" href="{PLAY_CHESS}">{ICON_PLAY}Chess Master</a><a class="btn" href="{PLAY_TAROT}">{ICON_PLAY}Daily Tarot</a></div>
</div>
</section>
''' + foot(lang, prefix, t, "/")


def build_support(lang, prefix, t):
    s = t["support"]
    faq = "".join(f"<details{' open' if i == 0 else ''}><summary>{q}</summary><p>{a}</p></details>" for i, (q, a) in enumerate(s["faq"]))
    stuck = s["stuck_p"].replace("{mail}", f'<a href="mailto:{MAIL}">{MAIL}</a>')
    return head(lang, prefix, t, f'{s["title"]} - Andrew Tech Solutions', s["p"], "/support/") + f'''
<div class="page-hero"><div class="wrap"><span class="eyebrow">{s["eyebrow"]}</span><h1>{s["h1a"]}<span class="grad">{s["h1b"]}</span></h1><p>{s["p"]}</p></div></div>
<div class="wrap two">
<div>
<h2 style="font-size:24px;margin:0 0 18px">{s["faq_h"]}</h2>
<div class="faq">{faq}</div>
<div class="prose" style="margin-top:40px"><h2>{s["stuck_h"]}</h2><p>{stuck}</p></div>
</div>
{side(prefix, t)}
</div>
''' + foot(lang, prefix, t, "/support/")


def build_terms(lang, prefix, t):
    s = t["terms"]
    secs = [(title, body.replace("{mail}", MAIL).replace("{support}", f"{prefix}/support/")) for title, body in s["s"]]
    toc = "".join(f'<li><a href="#{slug(x)}">{i + 1}. {x}</a></li>' for i, (x, _) in enumerate(secs))
    body = "".join(f'<h2 id="{slug(x)}">{i + 1}. {x}</h2>{y}' for i, (x, y) in enumerate(secs))
    note = f'<p class="pol-note">{s["note"]}</p>' if s["note"] else ""
    return head(lang, prefix, t, f'{s["title"]} - Andrew Tech Solutions', s["p"], "/terms/") + f'''
<div class="page-hero"><div class="wrap"><span class="eyebrow">{s["eyebrow"]}</span><h1>{s["h1"]}</h1><p>{s["p"]}</p><div class="date">{s["effective"]}</div></div></div>
<div class="wrap two">
<article class="prose">
<p class="lede">{s["lede"]}</p>
{note}
<ul class="toc">{toc}</ul>
{body}
</article>
{side(prefix, t)}
</div>
''' + foot(lang, prefix, t, "/terms/")


def build_privacy(lang, prefix, t):
    s = t["privacy"]
    bullets = "".join(f'<li><strong>{x}</strong> {y.replace("{mail}", MAIL)}</li>' for x, y in s["b"])
    note = f'<p class="pol-note" style="margin-top:0">{s["english_note"]}</p>' if s["english_note"] else ""
    return head(lang, prefix, t, f'{s["title"]} - Andrew Tech Solutions', s["p"], "/privacy/") + f'''
<div class="page-hero"><div class="wrap"><span class="eyebrow">{s["eyebrow"]}</span><h1>{s["h1a"]}<span class="grad">{s["h1b"]}</span></h1><p>{s["p"]}</p><div class="date">{s["effective"]}</div></div></div>
<div class="wrap two">
<article class="prose">
<h2 style="margin-top:0">{s["per_h"]}</h2>
<p>{s["per_p"]}</p>
<div class="grid4" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin:18px 0 14px">
<a class="tile" href="/privacy/chess-master/" style="text-decoration:none"><img src="/assets/chess-master.png" alt="" width="46" height="46" style="border-radius:12px;margin-bottom:14px"><h3>Chess Master</h3><p>{s["chess_p"]}</p></a>
<a class="tile" href="/privacy/daily-tarot/" style="text-decoration:none"><img src="/assets/daily-tarot.png" alt="" width="46" height="46" style="border-radius:12px;margin-bottom:14px"><h3>Daily Tarot</h3><p>{s["tarot_p"]}</p></a>
</div>
{note}
<h2>{s["all_h"]}</h2>
<ul>{bullets}</ul>
</article>
{side(prefix, t)}
</div>
''' + foot(lang, prefix, t, "/privacy/")


# ---------------- per-app privacy (English source, parsed from the app repos) ----------------
def parse_policy(path, pfx):
    h = open(path).read()
    h = re.sub(r"<style>.*?</style>", "", h, flags=re.S)
    g = lambda rx: re.search(rx, h, re.S)
    eyebrow = g(rf'<span class="{pfx}-eyebrow">(.*?)</span>').group(1).strip()
    blurb = g(rf'<header class="{pfx}-hero">.*?<p>(.*?)</p>').group(1).strip()
    chips = re.findall(rf'<span class="{pfx}-chip">(.*?)</span>', h, re.S)
    cards = re.findall(rf'<div class="{pfx}-card"><div class="ico">(.*?)</div><b>(.*?)</b><span>(.*?)</span></div>', h, re.S)
    intro = g(r'</nav>\s*(.*?)\s*<section').group(1).strip()
    secs = re.findall(rf'<section class="{pfx}-sec" id="{pfx}-(\d+)">\s*<h2><span class="{pfx}-num">\d+</span>(.*?)</h2>(.*?)</section>', h, re.S)
    foot_ = g(rf'<p class="{pfx}-foot">(.*?)</p>').group(1).strip()
    clean = lambda b: b.replace(f'class="{pfx}-path"', 'class="pol-path"').replace(f'class="{pfx}-note"', 'class="pol-note"').strip()
    return dict(eyebrow=eyebrow, blurb=blurb, chips=chips, cards=cards, intro=intro,
                secs=[(n, x.strip(), clean(b)) for n, x, b in secs], foot=foot_)


SCROLLSPY = """<script>
(function(){var links=[].slice.call(document.querySelectorAll('.pol-nav a[data-s]'));var secs=links.map(function(a){return document.getElementById(a.dataset.s)});
function act(){var y=window.scrollY+140,cur=secs[0];secs.forEach(function(s){if(s&&s.offsetTop<=y)cur=s});links.forEach(function(a){a.classList.toggle('on',a.dataset.s===cur.id)})}
window.addEventListener('scroll',act,{passive:true});act()})();
</script>"""

APPS = [
    ("chess-master", "Chess Master", "chess-master.png", "var(--gold)", "&#9822;",
     os.path.join(SRC, "game_chess/docs/privacy-policy-embed-en.html"), "cm"),
    ("daily-tarot", "Daily Tarot", "daily-tarot.png", "#c4b5fd", "&#10022;",
     os.path.join(SRC, "tarot-app/docs/privacy-policy-embed-en.html"), "dt"),
    ("plushie-blocks", "Plushie Blocks", "plushie-blocks.png", "#ffb4e6", "&#9638;",
     os.path.join(SRC, "block_puzzle/docs/privacy-policy-embed-en.html"), "bp"),
]


def build_policy(name, title, icon, accent, mark, path, pfx):
    t = T["en"]; p = t["policy"]
    d = parse_policy(path, pfx)
    page = f"/privacy/{name}/"
    toc = "".join(f'<li><a href="#s{n}" data-s="s{n}"><i>{n}</i><span>{x}</span></a></li>' for n, x, _ in d["secs"])
    body = "".join(f'<section class="pol-sec" id="s{n}"><div class="pol-num">{n.zfill(2)}</div><h2>{x}</h2>{b}</section>' for n, x, b in d["secs"])
    cards = "".join(f'<div class="pol-card rv"><div class="ico">{i}</div><b>{x}</b><span>{y}</span></div>' for i, x, y in d["cards"])
    chips = "".join(f'<span class="pol-chip">{c}</span>' for c in d["chips"])
    intro = d["intro"].replace("<p>", "").replace("</p>", "")
    # English-only page: canonical/hreflang point to itself.
    html = head("en", "", t, f"Privacy Policy - {title}", f"How the {title} app handles your information.", page)
    html = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">', "", html)
    html += f"""
<div class="page-hero pol-hero" style="--accent:{accent}">
<div class="wrap">
<div class="pol-hero-grid">
<div>
<span class="eyebrow">{p["legal"]} &middot; {d["eyebrow"]}</span>
<h1>Privacy <span class="grad">Policy</span></h1>
<p>{d["blurb"]}</p>
<div class="pol-chips">{chips}</div>
</div>
<div class="pol-hero-icon"><img src="/assets/{icon}" alt="{title} icon" width="128" height="128"><span class="mark">{mark}</span></div>
</div>
</div>
</div>
<div class="wrap">
<div class="pol-summary">{cards}</div>
<div class="pol-layout">
<aside class="pol-nav">
<div class="pol-nav-inner">
<strong>{p["contents"]}</strong>
<ol>{toc}</ol>
<a class="pol-all" href="/privacy/">&larr; {p["all"]}</a>
</div>
</aside>
<article class="pol-body">
<p class="pol-intro">{intro}</p>
{body}
<div class="pol-contact">
<div><h3>{p["q"]}</h3><p>{p["reply"]}</p></div>
<a class="btn" href="mailto:{MAIL}">{MAIL}</a>
</div>
<p class="pol-foot">{d["foot"]}</p>
</article>
</div>
</div>
{SCROLLSPY}
""" + foot("en", "", t, page)
    write(f"{page}index.html", html)


# ---------------- run ----------------
for lang, _, prefix in LANGS:
    t = T[lang]
    write(f"{prefix}/index.html", build_index(lang, prefix, t))
    write(f"{prefix}/support/index.html", build_support(lang, prefix, t))
    write(f"{prefix}/terms/index.html", build_terms(lang, prefix, t))
    write(f"{prefix}/privacy/index.html", build_privacy(lang, prefix, t))
for app in APPS:
    build_policy(*app)

# sitemap
urls = [f"{HOST}{p}{page}" for _, _, p in LANGS for page in PAGES] + [f"{HOST}/privacy/{n}/" for n, *_ in APPS]
write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
      "".join(f"<url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {HOST}/sitemap.xml\n")
print("ok", len(urls), "urls")
