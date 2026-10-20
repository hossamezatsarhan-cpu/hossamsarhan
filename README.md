# Hossam Ezzat Sarhan — Portfolio

Bilingual Arabic/English static portfolio for a Senior .NET Developer and Team Lead.

## Local preview

Run `python -m http.server 8765 --bind 127.0.0.1` from the repository and open http://127.0.0.1:8765.
No build or package installation is required. Bootstrap, icons and Cairo font load from external CDNs.

## Content

- `index.html`: profile, skills, career, education, certifications, selected projects and contact details.
- `apps/`: the three existing application showcases.
- `assets/css/style.css`: shared styles and responsive portfolio layouts.
- `assets/js/main.js`: language persistence, RTL/LTR styles and mobile navigation.

Experience and additional project summaries were taken from the supplied CV. Contact links use the user's latest email and phone. Existing application feature descriptions and images are retained; repeated unsupported numerical metrics were removed. No client outcomes, project URLs or testimonials were invented.

## Deployment

This checkout already has `CNAME` set to `hossamsarhan.com`. The public domain is served by GitHub Pages from the `main` branch at the repository root. Publishing updates uses the existing GitHub Pages workflow. The InterServer VPS serves separate application subdomains; the main portfolio does not require VPS configuration changes.

## Verification

Checked JavaScript syntax, local HTTP response, page links, image paths, section anchors, unique IDs and bilingual text attributes on all four pages. Manually checked the mobile preview, menu expansion and language switching in the browser.
