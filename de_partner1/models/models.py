-*- coding: utf-8 -*-

from odoo import models, fields, api
    _inherit = 'res.partner'
    
    father_name = fields.Char('Father Name')

# class de_partner1(models.Model):
#     _name = 'de_partner1.de_partner1'
#     _description = 'de_partner1.de_partner1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
