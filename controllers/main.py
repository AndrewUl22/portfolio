# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class PortfolioController(http.Controller):

    @http.route('/portfolio', type='http', auth='public', website=True, sitemap=True)
    def portfolio_page(self, **kwargs):
        """Публичная страница портфолио, доступная без логина."""
        values = {
            'name': 'Andrew',
            'tagline': 'Начинающий Odoo-разработчик',
            'github_url': 'https://github.com/YOUR_USERNAME/library',  # TODO: замени на свою ссылку
            'skills': [
                'Python', 'Odoo ORM', 'PostgreSQL',
                'XML Views', 'JavaScript', 'Owl Framework',
            ],
        }
        return request.render('portfolio.portfolio_page_template', values)
