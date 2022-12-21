from odoo import api, fields, models


class ResPartnerPrototype(models.Model):
    _name = "library.book.prototype"
    _inherit = "library.book"

    field_prototype_inherit = fields.Char(
        string="Test prototype inherit"
    )
