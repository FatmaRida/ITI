# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ItiStudent(models.Model):
    _name = 'iti.student'

    @api.depends('gender')
    def _compute_salary(self):
        dummy={}
        for record in self:
           if record.gender == 'm':
              record.salary = 5000
        else:
            record.salary=2000

    name = fields.Char()
    age = fields.Integer()
    email = fields.Char()
    image = fields.Binary()
    gender = fields.Selection([

        ('m', 'male'),
        ('f', 'female'),
    ])
    desc = fields.Text()
    join_data = fields.Datetime()
    date_of_birth = fields.Date()
    is_accepted = fields.Boolean()
    bio = fields.Html()
    salary=fields.Float(compute=_compute_salary)
    track_id = fields.Many2one('iti.track',string='Student Track')
    track_desc = fields.Text(related='track_id.desc' , store=True)
    skills_ids = fields.Many2many('iti.skill')
    course_line_ids = fields.One2many('iti.course.line', 'student_id')
