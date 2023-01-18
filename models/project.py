

from odoo import models, fields, api



class EnterpriseProject(models.Model):
    
    #Properties
    _name="enterprise.project"
    _description ="Proyecto empresarial"

    name = fields.Char(string ='Nombre del proyecto', required=True)
    
    startDate = fields.Date(string='Fecha de inicio')
    deadLine = fields.Date(string='Fecha final')
   
    description = fields.Text(string = 'Descripción')
    state = fields.Selection([
        ('draft','Análisis'),
        ('confirm','Desarrollo'),
        ('done','Finalizado'),
        ('cancel','Cancelado')
    ],string="Status",default='draft')
    
    worker_ids = fields.One2many('person.worker','name',string = 'Trabajadores asignados')

    
    

    #Métodos

    # Método que cambia la propiedad state para el botón del header
    def action_confirm(self):
        self.state = 'confirm'

    # Método que cambia la propiedad state para el botón del header
    def action_done(self):
        self.state = 'done'
    
    # Método que cambia la propiedad state para el botón del header
    def action_draft(self):
        self.state = 'draft'
    
    # Método que cambia la propiedad state para el botón del header
    def action_cancel(self):
        self.state = 'cancel'