from odoo import models, fields

class ItiTrack(models.Model):
    _name = 'iti.track'
    name = fields.Char()
    desc = fields.Text()
    student_ids = fields.One2many('iti.student','track_id')
