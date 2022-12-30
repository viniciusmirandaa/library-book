from odoo import models, fields, api


class LibraryBookCateg(models.Model):
    _name = "library.book.categ"

    name = fields.Char(
        string="Name"
    )



