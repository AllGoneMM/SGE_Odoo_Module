

from odoo import models, fields, api



class EnterpriseProject(models.Model):
    
    #Properties
    _name="enterprise.project"
    _inherit=['mail.thread','mail.activity.mixin']
    _description ="Proyecto empresarial"

    name = fields.Char(string ='Nombre del proyecto', required=True,tracking = True)
    
    startDate = fields.Date(string='Fecha de inicio',tracking = True)
    deadLine = fields.Date(string='Fecha final',tracking = True)
   
    description = fields.Text(string = 'Descripción',tracking = True)
    state = fields.Selection([
        ('draft','Análisis'),
        ('confirm','Desarrollo'),
        ('done','Finalizado'),
        ('cancel','Cancelado')
    ],string="Status",default='draft',tracking = True)
    
    worker_ids = fields.One2many('person.worker','name',string = 'Trabajadores asignados',tracking = True)
    # worker_count =fields.Integer(string='Número de empleados', compute='get_workers_count',tracking = True)
    
    project_lines = fields.One2many('enterprise.project.lines','project_id',string="Project Lines")

    
    #Métodos

    # def get_workers_count(self):
    #     count = self.env['person.worker'].search_count([('project_id', '=', self.id)])
    #     self.worker_count = count

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

class EnterpriseProjectLines(models.Model):
    _name="enterprise.project.lines"
    _description="Project Lines"

    worker_id = fields.Many2one('person.worker',string ='Trabajador/a asignado')
    worker_role =fields.Many2one('person.worker','role',string='Puesto de trabajo')
    project_id = fields.Many2one('enterprise.project', string ='Id Proyecto')