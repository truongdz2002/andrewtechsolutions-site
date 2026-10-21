#!/usr/bin/env python3
"""Generate the static pages for andrewtechsolutions-site (shared header/footer)."""
import os, re, sys

ROOT = sys.argv[1]
SRC = sys.argv[2]  # /Users/victor/Documents/personal
MAIL = "dodangtruong2002@gmail.com"
PLAY_CHESS = "https://play.google.com/store/apps/details?id=com.andrewtechsolutions.boardgames"
PLAY_TAROT = "https://play.google.com/store/apps/details?id=com.victor.tarot"

ICON_PLAY = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3.6 2.3 13.3 12l-9.7 9.7c-.4-.3-.6-.8-.6-1.4V3.7c0-.6.2-1.1.6-1.4zm1.3-.7c.3 0 .7.1 1 .3l11.4 6.5-2.6 2.6L4.9 1.6zm12.7 7.3 3.3 1.9c1 .6 1 1.9 0 2.5l-3.3 1.9-2.9-2.9 2.9-3.4zM5.9 22.1c-.3.2-.7.3-1 .3l9.8-9.4 2.6 2.6L5.9 22.1z"/></svg>'
ICON_APPLE = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.4 12.6c0-2.5 2-3.7 2.1-3.8-1.2-1.7-3-1.9-3.6-2-1.5-.2-3 .9-3.8.9s-2-.9-3.3-.9C6.1 6.9 4.5 7.9 3.6 9.4c-1.9 3.3-.5 8.1 1.3 10.8.9 1.3 2 2.7 3.4 2.7 1.4-.1 1.9-.9 3.5-.9s2.1.9 3.5.9 2.4-1.3 3.3-2.6c1-1.5 1.5-3 1.5-3.1-.1 0-2.9-1.1-2.9-4.6zM14 5.2c.7-.9 1.2-2.1 1.1-3.2-1 0-2.3.7-3 1.6-.7.8-1.3 2-1.1 3.2 1.1.1 2.3-.6 3-1.6z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="m8.5 12 2.3 2.3L15.5 9.6"/></svg>'

def head(title, desc, path=""):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://andrewtechsolutions.cloud{path}">
<meta property="og:image" content="https://andrewtechsolutions.cloud/assets/chess-master.png">
<meta name="theme-color" content="#060a13">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="canonical" href="https://andrewtechsolutions.cloud{path}">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="/"><i></i>Andrew Tech Solutions</a>
<nav><a href="/#apps">Apps</a><a href="/#why">Why us</a><a href="/support/">Support</a><a href="/privacy/">Privacy</a><a href="/terms/">Terms</a><a class="btn sm" href="/#apps">Get the apps</a></nav>
</div></header>
<main>
'''

FOOT = f'''</main>
<footer class="site"><div class="wrap">
<div class="fgrid">
<div><a class="brand" href="/"><i></i>Andrew Tech Solutions</a><p>Small, focused mobile apps for Android and iOS. No accounts, no tracking servers, your data stays on your device.</p></div>
<div><h4>Apps</h4><ul><li><a href="/#chess">Chess Master</a></li><li><a href="/#tarot">Daily Tarot</a></li></ul></div>
<div><h4>Legal</h4><ul><li><a href="/privacy/">Privacy Policy</a></li><li><a href="/terms/">Terms of Use</a></li><li><a href="/app-ads.txt">app-ads.txt</a></li></ul></div>
<div><h4>Help</h4><ul><li><a href="/support/">Support &amp; FAQ</a></li><li><a href="mailto:{MAIL}">Email us</a></li></ul></div>
</div>
<div class="fbot"><span>&copy; 2026 Andrew Tech Solutions. All rights reserved.</span><span>Made with care in Vietnam</span></div>
</div></footer>
<script>
(function(){{var els=document.querySelectorAll('.rv');if(!('IntersectionObserver' in window)){{els.forEach(function(e){{e.classList.add('in')}});return}}
var io=new IntersectionObserver(function(en){{en.forEach(function(x){{if(x.isIntersecting){{x.target.classList.add('in');io.unobserve(x.target)}}}})}},{{threshold:.12}});
els.forEach(function(e){{io.observe(e)}})}})();
</script>
</body>
</html>
'''

def write(rel, html):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(html)

# ---------------- chess board ----------------
# Starting position with a highlighted knight move (Nf3) for life.
rows = ["rnbqkbnr", "pppppppp", "........", "........", "........", ".....N..", "PPPPP.PP", "RNBQKB.R"]
glyph = {"k":"&#9818;","q":"&#9819;","r":"&#9820;","b":"&#9821;","n":"&#9822;","p":"&#9823;",
         "K":"&#9812;","Q":"&#9813;","R":"&#9814;","B":"&#9815;","N":"&#9816;","P":"&#9817;"}
cells = []
for r, row in enumerate(rows):
    for c, ch in enumerate(row):
        cls = []
        if ch.isupper(): cls.append("w")
        if (r, c) == (5, 5): cls.append("hl")
        if (r, c) == (7, 6): cls.append("hl")
        if (r, c) in [(3, 4), (3, 6), (4, 3), (4, 7)]: cls.append("dot")
        cells.append(f'<span class="{" ".join(cls)}">{glyph.get(ch, "")}</span>')
board = "".join(cells)

games = ["Chess", "Chess960", "Xiangqi", "Jieqi", "Go", "Shogi", "Janggi", "Gomoku", "Othello", "Checkers",
         "Connect Four", "Ô Ăn Quan", "Cờ Gánh", "Ludo"]
marquee_items = "".join(f"<li>{g}</li>" for g in games + ["Card of the Day", "Celtic Cross", "78 cards", "Offline", "No account"])

index = head("Andrew Tech Solutions", "Mobile apps by Andrew Tech Solutions: Chess Master, 14 classic board games in one app, and Daily Tarot, a calm daily tarot companion.", "/") + f'''
<div class="wrap"><section class="hero">
<div>
<span class="eyebrow">Mobile apps &middot; Android &amp; iOS</span>
<h1>Simple, well-made <span class="grad">mobile apps.</span></h1>
<p class="lead">Classic board games and a calm daily tarot companion. Built to be fast, beautiful and offline. No accounts, no tracking servers. Your data never leaves your device.</p>
<div class="cta"><a class="btn" href="#apps">Explore the apps</a><a class="btn ghost" href="/support/">Get support</a></div>
<ul class="stats">
<li><b><span>14</span></b>board games in one app</li>
<li><b><span>78</span></b>tarot cards explained</li>
<li><b><span>100%</span></b>offline play</li>
<li><b><span>0</span></b>accounts required</li>
</ul>
</div>
<div class="phones">
<div class="orb one"></div><div class="orb two"></div>
<div class="phone a"><img src="/assets/shots/tarot-1-home.png" alt="Daily Tarot home screen" width="250" height="536" loading="eager"></div>
<div class="phone b"><img src="/assets/shots/tarot-5-reading.png" alt="Daily Tarot reading screen" width="250" height="536"></div>
</div>
</section></div>

<div class="marquee"><ul>{marquee_items}{marquee_items}</ul></div>

<section id="apps" class="wrap">
<div class="sec-head rv"><span class="eyebrow">Our apps</span><h2>Two apps. One promise: <span class="grad">it just works.</span></h2><p>Each app is small, focused and finished. Install, open, play. Nothing to sign up for.</p></div>

<div id="chess" class="show">
<div class="copy rv">
<img class="icon" src="/assets/chess-master.png" alt="Chess Master icon" width="76" height="76">
<span class="tag">Strategy &middot; 14 games</span>
<h2>Chess Master: Xiangqi, Go</h2>
<p>Fourteen classic board games from around the world in one beautiful app. Play a friend on the same phone or tablet, or challenge the computer at four levels, entirely offline.</p>
<div class="games">{"".join(f"<span>{g}</span>" for g in games)}</div>
<ul class="feat">
<li>{CHECK}<span><b>Smart AI opponents.</b> Easy, Normal, Hard and a Master level for a real challenge.</span></li>
<li>{CHECK}<span><b>Pass and play.</b> Two players on one device, with undo, hints and move history.</span></li>
<li>{CHECK}<span><b>Vietnamese folk games.</b> Ô Ăn Quan and Cờ Gánh, faithfully recreated.</span></li>
</ul>
<div class="cta"><a class="btn" href="{PLAY_CHESS}">{ICON_PLAY}Google Play</a><a class="btn ghost soon" href="#">{ICON_APPLE}App Store soon</a><span class="meta">Free &middot; Premium removes ads</span></div>
<p style="margin:14px 0 0;font-size:14px"><a href="/privacy/chess-master/">Privacy policy for Chess Master</a></p>
</div>
<div class="visual rv d1">
<div class="glow" style="background:var(--gold);opacity:.18"></div>
<div class="board-wrap">
<div class="board">{board}</div>
<div class="hud"><span>Chess &middot; <b>Nf3</b></span><span class="lvl">★ Master level</span><span>Move <b>1</b></span></div>
</div>
</div>
</div>

<div id="tarot" class="show flip">
<div class="copy rv">
<img class="icon" src="/assets/daily-tarot.png" alt="Daily Tarot icon" width="76" height="76">
<span class="tag">Lifestyle &middot; Reflection</span>
<h2>Daily Tarot: Card Reading</h2>
<p>A calm, beautiful companion for reflection. Reveal one card each morning, ask a question with a spread, and learn what every one of the 78 cards means.</p>
<ul class="feat">
<li>{CHECK}<span><b>Card of the Day.</b> A single card, a short message and one small thing to try. Home screen widget included.</span></li>
<li>{CHECK}<span><b>10 spreads.</b> From Yes or No to the classic Celtic Cross, with reversed cards optional.</span></li>
<li>{CHECK}<span><b>Learn tarot.</b> All 78 cards with upright and reversed meanings, lessons and a quiz.</span></li>
<li>{CHECK}<span><b>Your own deck.</b> Draw physical cards and enter them for a full interpretation.</span></li>
</ul>
<div class="cta"><a class="btn" href="{PLAY_TAROT}">{ICON_PLAY}Google Play</a><a class="btn ghost soon" href="#">{ICON_APPLE}App Store soon</a><span class="meta">Free</span></div>
<p style="margin:14px 0 0;font-size:14px"><a href="/privacy/daily-tarot/">Privacy policy for Daily Tarot</a></p>
</div>
<div class="visual rv d1">
<div class="glow" style="background:var(--c2)"></div>
<div class="tarot-visual">
<div class="phone l"><img src="/assets/shots/tarot-3-spread.png" alt="Choosing a tarot spread" width="240" height="515" loading="lazy"></div>
<div class="phone r"><img src="/assets/shots/tarot-2-daily.png" alt="Card of the day" width="240" height="515" loading="lazy"></div>
</div>
</div>
</div>
</section>

<section id="why" class="wrap">
<div class="sec-head rv"><span class="eyebrow">Principles</span><h2>Built the way we'd want <span class="grad">our own apps built.</span></h2><p>A few rules we never break, in every app we ship.</p></div>
<div class="grid4">
<div class="tile rv"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3 4 7v5c0 5 3.4 8.4 8 9 4.6-.6 8-4 8-9V7l-8-4z"/><path d="m9 12 2 2 4-4"/></svg></div><h3>Privacy by default</h3><p>No account, no login, no servers of ours. Games, readings and settings stay on your phone.</p></div>
<div class="tile rv d1"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5 2 10a15 15 0 0 1 20 0l-3 2.5"/><path d="M8.5 16 7 14.6a8 8 0 0 1 10 0L15.5 16"/><circle cx="12" cy="19" r="1.2"/><path d="m3 3 18 18"/></svg></div><h3>Works offline</h3><p>Everything runs on the device. On a plane, underground or in the countryside, it all just works.</p></div>
<div class="tile rv d2"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h7l-1 8 9-12h-7l1-8z"/></svg></div><h3>Fast and light</h3><p>Small downloads, instant launch, smooth animations even on older phones.</p></div>
<div class="tile rv d3"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-4.6-7-11a7 7 0 0 1 14 0c0 6.4-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg></div><h3>Made in Vietnam</h3><p>Designed and built by a small team that answers its own support email, usually within two days.</p></div>
</div>
</section>

<section class="wrap">
<div class="band rv">
<h2>Ready to play?</h2>
<p>Both apps are free on Google Play. iOS versions are on the way.</p>
<div class="cta"><a class="btn" href="{PLAY_CHESS}">{ICON_PLAY}Chess Master</a><a class="btn" href="{PLAY_TAROT}">{ICON_PLAY}Daily Tarot</a></div>
</div>
</section>
''' + FOOT
write("index.html", index)

# ---------------- support ----------------
side = f'''<aside class="side">
<div class="card contact"><h3>Contact us</h3><p>We usually reply within 2 business days.</p><a class="mail" href="mailto:{MAIL}">{MAIL}</a></div>
<div class="card"><h3>Our apps</h3><ul class="list">
<li><a href="/#chess"><img src="/assets/chess-master.png" alt="">Chess Master</a></li>
<li><a href="/#tarot"><img src="/assets/daily-tarot.png" alt="">Daily Tarot</a></li></ul></div>
<div class="card"><h3>Legal</h3><ul class="list"><li><a href="/privacy/">Privacy Policy</a></li><li><a href="/terms/">Terms of Use</a></li></ul></div>
</aside>'''

faq = [
 ("Do I need an account?", "No. None of our apps require sign-up or login, and we do not run servers that store your data."),
 ("How do I delete my data?", "All data is stored on your device. Use the app's Settings to clear history, or uninstall the app to remove everything."),
 ("How do I restore a purchase (Chess Master Premium)?", "Reinstall the app and open the Premium screen. Purchases are tied to your Google Play or Apple ID account and restore automatically. If not, contact us with your order number."),
 ("How do I cancel a subscription?", "Subscriptions are managed by the store, not by us. On Android open Google Play, then Payments &amp; subscriptions. On iOS open Settings, tap your name, then Subscriptions."),
 ("How do I control ads?", "Ads are served by Google AdMob. You can reset or opt out of ad personalisation in your device's Google or Apple privacy settings. Chess Master Premium removes ads entirely."),
 ("The app crashes or a game behaves strangely. What should I send?", "The app name and version, your device model and OS version, and what you did just before it happened. A screenshot or screen recording helps a lot."),
 ("Can I request a new game or feature?", "Yes, please. Email us with your idea. Many games in Chess Master were added because players asked."),
]
support = head("Support - Andrew Tech Solutions", "Help, FAQ and contact for Chess Master and Daily Tarot.", "/support/") + f'''
<div class="page-hero"><div class="wrap"><span class="eyebrow">Support</span><h1>How can we <span class="grad">help?</span></h1><p>Answers to common questions about Chess Master and Daily Tarot, and how to reach a human when you need one.</p></div></div>
<div class="wrap two">
<div>
<h2 style="font-size:24px;margin:0 0 18px">Frequently asked questions</h2>
<div class="faq">{"".join(f"<details{' open' if i==0 else ''}><summary>{q}</summary><p>{a}</p></details>" for i,(q,a) in enumerate(faq))}</div>
<div class="prose" style="margin-top:40px"><h2>Still stuck?</h2><p>Email <a href="mailto:{MAIL}">{MAIL}</a>. Please include the app name, your device model and OS version, and what happened. Screenshots help a lot.</p></div>
</div>
{side}
</div>
''' + FOOT
write("support/index.html", support)

# ---------------- terms ----------------
terms_sections = [
 ("License", "<p>We grant you a personal, non-exclusive, non-transferable, revocable license to use the App on a device you own or control, for personal, non-commercial purposes, subject to these Terms and the rules of the store you downloaded it from (Google Play or Apple App Store).</p>"),
 ("Restrictions", "<ul><li>Do not copy, modify, reverse engineer, decompile or create derivative works of the App.</li><li>Do not remove copyright or trademark notices.</li><li>Do not use the App for any unlawful purpose or to interfere with its operation.</li></ul>"),
 ("Purchases and subscriptions", "<p>Some Apps offer optional in-app purchases or subscriptions (for example Chess Master Premium). Payment is collected by Google Play or Apple, under their terms. Subscriptions renew automatically unless cancelled at least 24 hours before the end of the current period, and can be managed or cancelled in your store account settings. Refunds are handled by the store according to its policy.</p><p>For Apps distributed through the Apple App Store, Apple's Standard End User License Agreement (EULA) also applies: <a href=\"https://www.apple.com/legal/internet-services/itunes/dev/stdeula/\">apple.com/legal/internet-services/itunes/dev/stdeula</a>.</p>"),
 ("Advertising", "<p>Free versions of our Apps may display ads served by Google AdMob. See each App's privacy policy for details.</p>"),
 ("Content disclaimer", "<p>Daily Tarot is provided for entertainment and personal reflection only. It does not provide medical, legal, financial or other professional advice.</p>"),
 ("Intellectual property", "<p>The Apps, including their code, design and artwork, are owned by us or our licensors and are protected by copyright and other laws. Game names such as Chess, Xiangqi or Go refer to traditional public-domain games.</p>"),
 ("Disclaimer of warranties", "<p>The Apps are provided \"as is\" and \"as available\" without warranties of any kind, express or implied. We do not guarantee that the Apps will be error-free or uninterrupted.</p>"),
 ("Limitation of liability", "<p>To the maximum extent permitted by law, we are not liable for any indirect, incidental, special or consequential damages arising from your use of the Apps. Our total liability shall not exceed the amount you paid us for the App in the 12 months before the claim.</p>"),
 ("Termination", "<p>We may suspend or terminate your license if you breach these Terms. You may stop using the App at any time by uninstalling it.</p>"),
 ("Changes", "<p>We may update these Terms from time to time. The effective date above will change and continued use of the App after an update means you accept the new Terms.</p>"),
 ("Contact", f"<p>Email <a href=\"mailto:{MAIL}\">{MAIL}</a> or visit the <a href=\"/support/\">support page</a>.</p>"),
]
def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
terms = head("Terms of Use - Andrew Tech Solutions", "Terms of use for apps published by Andrew Tech Solutions.", "/terms/") + f'''
<div class="page-hero"><div class="wrap"><span class="eyebrow">Legal</span><h1>Terms of Use</h1><p>The rules for using Chess Master, Daily Tarot and any other app we publish.</p><div class="date">EFFECTIVE 2026-10-21</div></div></div>
<div class="wrap two">
<article class="prose">
<p class="lede">These Terms of Use ("Terms") govern your use of the mobile applications published by Andrew Tech Solutions ("we", "us"), including Chess Master and Daily Tarot (each an "App"). By downloading or using an App you agree to these Terms.</p>
<ul class="toc">{"".join(f'<li><a href="#{slug(t)}">{i+1}. {t}</a></li>' for i,(t,_) in enumerate(terms_sections))}</ul>
{"".join(f'<h2 id="{slug(t)}">{i+1}. {t}</h2>{b}' for i,(t,b) in enumerate(terms_sections))}
</article>
{side}
</div>
''' + FOOT
write("terms/index.html", terms)

# ---------------- privacy index ----------------
privacy = head("Privacy Policy - Andrew Tech Solutions", "Privacy policies for apps published by Andrew Tech Solutions.", "/privacy/") + f'''
<div class="page-hero"><div class="wrap"><span class="eyebrow">Legal</span><h1>Privacy <span class="grad">Policy</span></h1><p>We build apps that keep your data on your device. No accounts, no servers of ours storing personal information.</p><div class="date">EFFECTIVE 2026-10-21</div></div></div>
<div class="wrap two">
<article class="prose">
<h2 style="margin-top:0">Per-app policies</h2>
<p>Each app has its own detailed policy covering exactly what it stores and which third parties are involved:</p>
<div class="grid4" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin:18px 0 10px">
<a class="tile" href="/privacy/chess-master/" style="text-decoration:none"><img src="/assets/chess-master.png" alt="" width="46" height="46" style="border-radius:12px;margin-bottom:14px"><h3>Chess Master</h3><p>Board games, AdMob ads, Google Play purchases.</p></a>
<a class="tile" href="/privacy/daily-tarot/" style="text-decoration:none"><img src="/assets/daily-tarot.png" alt="" width="46" height="46" style="border-radius:12px;margin-bottom:14px"><h3>Daily Tarot</h3><p>Readings, notifications, AdMob ads, local backups.</p></a>
</div>
<h2>What applies to all our apps</h2>
<ul>
<li><strong>No account, no login.</strong> Game results, readings, settings and history are stored only on your device and never sent to us.</li>
<li><strong>Advertising.</strong> Free versions show ads from Google AdMob, which may use your advertising identifier. See <a href="https://policies.google.com/privacy">Google's privacy policy</a> and your device's ad settings.</li>
<li><strong>Payments.</strong> In-app purchases are processed by Google Play or Apple. We never see your payment details.</li>
<li><strong>Children.</strong> Our apps are not directed at children under 13 and we do not knowingly collect personal information from them.</li>
<li><strong>Your rights.</strong> You can delete all app data from the app's Settings or by uninstalling. For any request, email <a href="mailto:{MAIL}">{MAIL}</a>.</li>
</ul>
</article>
{side}
</div>
''' + FOOT
write("privacy/index.html", privacy)

# ---------------- per-app privacy (parsed from the app repos' embeds, rendered natively) ----------------
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
    foot = g(rf'<p class="{pfx}-foot">(.*?)</p>').group(1).strip()
    def clean(b):
        b = b.replace(f'class="{pfx}-path"', 'class="pol-path"').replace(f'class="{pfx}-note"', 'class="pol-note"')
        return b.strip()
    return dict(eyebrow=eyebrow, blurb=blurb, chips=chips, cards=cards, intro=intro,
                secs=[(n, t.strip(), clean(b)) for n, t, b in secs], foot=foot)

SCROLLSPY = """<script>
(function(){var links=[].slice.call(document.querySelectorAll('.pol-nav a[data-s]'));var secs=links.map(function(a){return document.getElementById(a.dataset.s)});
function act(){var y=window.scrollY+140,cur=secs[0];secs.forEach(function(s){if(s&&s.offsetTop<=y)cur=s});links.forEach(function(a){a.classList.toggle('on',a.dataset.s===cur.id)})}
window.addEventListener('scroll',act,{passive:true});act()})();
</script>"""

apps = [
    ("chess-master", "Chess Master", "chess-master.png", "var(--gold)", "&#9822;",
     os.path.join(SRC, "game_chess/docs/privacy-policy-embed-en.html"), "cm", "/privacy/chess-master/"),
    ("daily-tarot", "Daily Tarot", "daily-tarot.png", "#c4b5fd", "&#10022;",
     os.path.join(SRC, "tarot-app/docs/privacy-policy-embed-en.html"), "dt", "/privacy/daily-tarot/"),
]
for name, title, icon, accent, mark, path, pfx, url in apps:
    d = parse_policy(path, pfx)
    toc = "".join(f'<li><a href="#s{n}" data-s="s{n}"><i>{n}</i><span>{t}</span></a></li>' for n, t, _ in d["secs"])
    body = "".join(f'<section class="pol-sec" id="s{n}"><div class="pol-num">{n.zfill(2)}</div><h2>{t}</h2>{b}</section>' for n, t, b in d["secs"])
    cards = "".join(f'<div class="pol-card rv"><div class="ico">{i}</div><b>{t}</b><span>{s_}</span></div>' for i, t, s_ in d["cards"])
    chips = "".join(f'<span class="pol-chip">{c}</span>' for c in d["chips"])
    intro = d["intro"].replace("<p>", "").replace("</p>", "")
    html = head(f"Privacy Policy - {title}", f"How the {title} app handles your information.", url) + f"""
<div class="page-hero pol-hero" style="--accent:{accent}">
<div class="wrap">
<div class="pol-hero-grid">
<div>
<span class="eyebrow">Legal &middot; {d["eyebrow"]}</span>
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
<strong>Contents</strong>
<ol>{toc}</ol>
<a class="pol-all" href="/privacy/">&larr; All policies</a>
</div>
</aside>
<article class="pol-body">
<p class="pol-intro">{intro}</p>
{body}
<div class="pol-contact">
<div><h3>Questions about your privacy?</h3><p>We usually reply within a few days.</p></div>
<a class="btn" href="mailto:{MAIL}">{MAIL}</a>
</div>
<p class="pol-foot">{d["foot"]}</p>
</article>
</div>
</div>
{SCROLLSPY}
""" + FOOT
    write(f"privacy/{name}/index.html", html)

print("ok")
