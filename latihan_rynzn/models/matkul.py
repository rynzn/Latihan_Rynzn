from odoo import models, fields, api, _
from odoo.exceptions import UserError

class Matkul(models.Model):
    _name = 'matkul.matkul'

    name = fields.Char(string='Name')
    kode = fields.Char(string='Kode')
    kelas_ids = fields.Many2many(
        comodel_name='kelas.kelas', 
        string='Kelas'
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Dosen Penagampu',
        domain=[("is_dosen", "=", "True")],
    )
    
    