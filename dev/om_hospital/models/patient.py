from odoo import api, fields, models
class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Record"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    is_child= fields.Boolean(string='Is Child?')
    notes = fields.Text(string='Notes')
    gender = fields.Selection([('male','Male'),('female','Female'),('Others' ,'others')],string="Gender")

