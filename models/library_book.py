from odoo import api, models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = "Library Book"
    _rec_name = "short_name"
    _order = "date_release desc, name"

    publisher_id = fields.Many2one(
        string="Publisher",
        comodel_name="res.partner",
        ondelete='restrict',
        domain=[('is_company', '=', True)]
    )

    name = fields.Char(
        string='Title',
        required=True
    )

    date_release = fields.Date(
        string='Release Date'
    )

    short_name = fields.Char(
        string='Short Title',
        translate=True,
        index=True
    )

    author_ids = fields.Many2many(
        comodel_name='res.partner',
        string='Authors',
        domain=[('is_company', '=', False)]
    )

    notes = fields.Text(
        string='Internal Notes'
    )

    state = fields.Selection(
        [('draft', 'Not Available'),
         ('available', 'Available'),
         ('lost', 'Lost')],
        string='State'
    )

    description = fields.Html(
        string='Description',
        sanitize=True,
        strip_style=False
    )

    cover = fields.Binary(
        string='Book Cover'
    )

    out_of_print = fields.Boolean(
        string='Out of Print?'
    )

    date_updated = fields.Datetime(
        string='Last Updated'
    )

    pages = fields.Integer(
        string='Number of Pages',
        groups='library.group_library_admin',
        states={'lost': [('readonly', True)]},
        help='Total book page count',
        company_dependent=False
    )

    reader_rating = fields.Float(
        string='Reader Average Rating',
        digits=(14, 4)
    )

    currency_id = fields.Many2one(
        string="Currency",
        comodel_name="res.currency"
    )

    retail_price = fields.Monetary(
        string="Retail Price",
        currency_field="currency_id"
    )

    def name_get(self):
        result = []
        rec_name = "%s / (%s)" % (self.name, self.date_release)
        result.append((self.id, rec_name))
        return result
