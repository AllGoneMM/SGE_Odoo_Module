

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
        ('draft','Borrador'),
        ('wip','En progreso'),
        ('done','Finalizado'),
        ('cancel','Cancelado')
    ],string="Status",default='Borrador')
    
    

    #Métodos

    # Método que cambia la propiedad state para el botón del header
    def action_wip(self):
        self.state = 'wip'

    # Método que cambia la propiedad state para el botón del header
    def action_done(self):
        self.state = 'done'
    
    # Método que cambia la propiedad state para el botón del header
    def action_draft(self):
        self.state = 'draft'
    
    # Método que cambia la propiedad state para el botón del header
    def action_cancel(self):
        self.state = 'cancel'