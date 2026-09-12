# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class PortfolioController(http.Controller):

    @http.route('/portfolio', type='http', auth='public', website=True, sitemap=True)
    def portfolio_page(self, **kwargs):
        """Public portfolio page, accessible without login."""
        values = {
            'name': 'Andrew',
            'tagline': 'Aspiring Odoo Developer',
            'github_url': 'https://github.com/AndrewUl22/library',  # TODO: replace with your link
            'skills': [
                'Python', 'Odoo ORM', 'PostgreSQL',
                'XML Views', 'JavaScript', 'Owl Framework',
            ],
        }
        return request.render('portfolio.portfolio_page_template', values)
