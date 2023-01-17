# -*- coding: utf-8 -*-
{
    'name': "SGE Módulo - Gestor de Proyectos",

    'summary': """
       Gestor de proyectos""",

    'description': """
       Módulo para organizar y asignar proyectos a los distintos empleados de la empresa
    """,

    'author': "Pablo Muñoz Martínez",
    'website': "https://aulavirtual.murciaeduca.es/course/view.php?id=86079",
    'category': 'Productivity',
    'version': '0.1',
    'instalable':True,
    'application':True,
    'auto_install':False,
    

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/worker.xml',
        'views/project.xml',
    
    
        'security/ir.model.access.csv'
        
    ],



    # only loaded in demonstration mode
    'demo': [],
}
