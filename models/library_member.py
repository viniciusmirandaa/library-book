from odoo import api, models, fields


class LibraryMember(models.Model):
    _name = "library.member"

    partner_id = fields.Many2one('res.partner',
                                 ondelete='cascade', delegate=True)
    date_start = fields.Date('Member Since')
    date_end = fields.Date('Termination Date')
    member_number = fields.Char()
    date_of_birth = fields.Date('Date of birth')
