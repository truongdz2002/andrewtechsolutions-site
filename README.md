# andrewtechsolutions.cloud

Static site: no build step. Open `index.html` in a browser to preview.

Pages: `/` (apps), `/support/`, `/privacy/` (+ one page per app), `/terms/`, `/app-ads.txt`.

## Deploy on GitHub Pages
1. Create a GitHub repo and push this folder (`git init && git add . && git commit -m "site"`).
2. Settings > Pages > Source: Deploy from branch `main`, folder `/ (root)`.
3. Settings > Pages > Custom domain: `andrewtechsolutions.cloud` (the `CNAME` file is already here). Tick "Enforce HTTPS" once the certificate is issued.
4. At the DNS provider add:
   - `A` records for `@` → 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
   - `CNAME` for `www` → `truongdz2002.github.io`

## Updating privacy policies
Source of truth stays in each app repo (`game_chess/docs/privacy-policy-embed-en.html`,
`tarot-app/docs/privacy-policy-embed-en.html`, `translation-app/privacy_policy.html`).
Re-copy them into `privacy/<app>/index.html` when they change.

`app-ads.txt` must keep both publisher lines (shared with another AdMob account).
