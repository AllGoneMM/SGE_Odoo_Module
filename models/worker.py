# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api




# Definimos modelo que representara los datos del trabajador de la empresa
class PersonWorker(models.Model):

    # Propiedades

    # Nombre que identifica a esta clase para acceder desde los XML
    _name="person.worker"
    _description ="Trabajador de la empresa"

    # Nombre del empleado 
    name = fields.Char(string ='Nombre', required=True)
    
    # Edad del empleado
    age = fields.Integer(string ='Edad')
    
    # Género del empleado
    gender = fields.Selection([
        ('male','Hombre'),
        ('female','Mujer'),
        ('other','Otros'),
    ],required=True,default='other',string="Género")

       # Rama técnica del empleado
    role = fields.Selection([
        ('backend','Back-end developer'),
        ('frontend','Front-end developer'),
        ('devops','Dev Ops'),
        ('fullStack','Full-stack developer'),
        ('projectManager','Project manager'),
    ],required=True,default='backend',string ="Puesto de trabajo")
    
    # Rama profesional del empleado

    description = fields.Text(string = 'Descripción')

    project_id = fields.Many2one('enterprise.project', string="Proyecto asignado", required=True)

    deadLine = fields.Date(string='Fecha final',related='project_id.deadLine',tracking=True)
    
    

    #Métodos

    @api.onchange('project_id')
    def onchange_project_id(self):
        if self.project_id:
            if self.project_id.deadLine:
                self.deadLine = self.project_id.deadLine
   