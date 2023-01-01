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

    categ_id = fields.Many2one(
        comodel_name="library.book.categ",
        string="Category"
    )

    retail_price = fields.Monetary(
        string="Retail Price",
        currency_field="currency_id"
    )

    test_prototype_inherit = fields.Char(
    )

    ref_doc_id = fields.Reference(
        selection='_referencable_models',
        string='Reference Document')

    record_set_operations_computed = fields.Integer(compute='record_set_operations')

    get_metadata_computed = fields.Integer(compute='get_record_metadata')

    def avg_retail_price_per_category(self):
        grouped_result = self.read_group(
            domain=[('retail_price', "!=", False)],  # domain
            fields=['categ_id', 'retail_price:avg'],  # fields to access
            groupby=['categ_id']  # group_by
        )
        return grouped_result

    @api.model
    def _referencable_models(self):
        models = self.env['ir.model'].search([
            ('field_id.name', '=', 'message_ids')])
        return [(x.model, x.name) for x in models]

    def name_get(self):
        result = []
        rec_name = "%s / (%s)" % (self.name, self.date_release)
        result.append((self.id, rec_name))
        return result

    def compute_field(self):
        book_ids = self.search([])

        sorted_book = book_ids.sorted(key='name')
        sorted_book2 = book_ids.sorted(key='name', reverse=True)

        filtered_book = book_ids.filtered('name')
        filtered_book2 = book_ids.filtered(lambda lm: len(lm.author_ids) > 1)

        mapped_book = book_ids.mapped('author_ids.email')
        mapped_book2 = book_ids.mapped('name')
        mapped_book3 = book_ids.mapped('author_ids')
        mapped_book4 = book_ids.mapped(lambda lm: lm.author_ids.name)
        mapped_book5 = book_ids.mapped(lambda lm: lm.name)
        mapped_book6 = book_ids.mapped(lambda lm: lm.author_ids)

        self.record_set_operations_computed = 1

    def get_record_metadata(self):
        metadata = self.get_metadata()
        record = self.env.ref('library-book.3')
