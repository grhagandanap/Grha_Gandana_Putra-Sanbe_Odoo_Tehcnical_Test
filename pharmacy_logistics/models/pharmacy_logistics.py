# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pharmacy_logistics(models.Model):
#     _name = 'pharmacy_logistics.pharmacy_logistics'
#     _description = 'pharmacy_logistics.pharmacy_logistics'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import api, fields, models


class Logistics(models.Model):
    _name = "pharmacy.logistics"
    _description = "pharmacy logistics"

    name = fields.Char(string="Name", required=True)
    product = fields.Many2one("product.product", string="Product")
    supplier = fields.Many2one("res.partner", string="Supplier")
    quantity = fields.Float("Quantity")
    arrival_date = fields.Date("Arrival Date")
    notes = fields.Text("Notes")

    def action_import_csv(self):
        print("Button Clicked")