# Portfolio — Odoo Website Portfolio Page

A public page at `/portfolio`, built into Odoo through the Website module and a QWeb template. It showcases my [`library`](https://github.com/AndrewUl22/library) project along with some basic info about me.

## Installation

1. Copy the `portfolio` folder into `addons/` (next to `library`):

```bash
cp -r portfolio /path/to/odoo/addons/
```

2. Install the module (requires the `website` module, which ships with Odoo by default — no separate installation needed):

```bash
./odoo-bin -d mydb --addons-path=addons,odoo/addons -i portfolio --dev=all
```

3. Open `http://localhost:8069/portfolio` — no login required, the page is public.

## TODO

- Replace placeholders in `controllers/main.py` (`name`, `github_url`, email in the template) with real data
- Add screenshots of the `library` interface (book form, loan list) to `static/description/` or an external image host, and embed them in the template via `<img t-att-src="...">`
- Once `library` is published on GitHub, update `github_url`
- Optional: add a photo, LinkedIn link, short "about me" — currently a placeholder, not final copy

## Ideas for further improvement (optional, but a nice touch)

- Replace the static `skills` list with an `ir.model`-backed one (good practice for dynamic QWeb templates driven by database data)
- Add a simple contact form via `type='http', methods=['POST']`
- Add a live-stats section from `library` (number of books, number of loans) — a good excuse to practice ORM queries (`self.env['library.book'].search_count([])`)