{
    'name': 'Portfolio',
    'version': '1.0',
    'summary': 'Публичная страница-портфолио на технологиях Odoo (Website + QWeb)',
    'description': """
Учебный модуль: страница портфолио, встроенная в Odoo Website.
Витрина проекта library (модели, репозиторий) + информация о себе.
""",
    'category': 'Website',
    'author': 'Your Name',
    'depends': ['website'],
    'data': [
        'views/portfolio_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'portfolio/static/src/css/portfolio.css',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
