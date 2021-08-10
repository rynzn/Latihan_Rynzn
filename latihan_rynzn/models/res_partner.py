from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthday = fields.Date(
        string='Birthday'
    )
    age = fields.Integer(
        string="Age",
        compute='_get_age',
        readonly=True
    )
    is_dosen = fields.Boolean(
        string="Dosen"
    )
    kelas_id = fields.Many2one(
        comodel_name='kelas.kelas',
        string="Kelas",
    )

    @api.constrains('birthday')
    def _check_birthday(self):
        if self.birthday > fields.Date.today():
            raise models.ValidationError(
                'Release Date Must be in the Past'
            )

    @api.depends('birthday')
    def _get_age(self):
        today = fields.Date.today() 
        if self.birthday:
            age = today - self.birthday
            self.age = int(age.days/365)
        else:
            self.age = 0