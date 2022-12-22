from odoo import api, fields, models


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = _name

    authored_book_ids = fields.Many2many(
        comodel_name='library.book',
        string='Authored Books',
    )

    published_books_ids = fields.One2many(
        string="Published Books",
        comodel_name="library.book",
        inverse_name="publisher_id"
    )

    test_extension_inherit = fields.Char(
        string='Field Test'
    )
