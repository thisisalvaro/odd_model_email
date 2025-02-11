{
    'name': 'Auto Invoice',
    'version': '1.0',
    'category': 'Sales',
    'author': 'Tu Nombre',
    'depends': ['sale', 'account'],  # Dependencias para las ventas y contabilidad
    'data': [
        'data/ir_cron.xml',  # Archivo para la tarea programada
    ],
}
