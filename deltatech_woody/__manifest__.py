# -*- coding: utf-8 -*-
{
    "name": "Deltatech Woody",
    'version': '10.0.1.0.0',
    "author": "Terrabit, Dorin Hongu",
    "website": "www.terrabit.ro",
    "summary": 'Import files from Woody',
    "description": """,

Functionalitati:

    - import fisiere din Woody

    """,

    "category": "Manufacturing",
    "depends": ['product','mrp','product_dimension','deltatech_optimik'],

    "data": [
        'wizard/woody_wizard_view.xml',
        'data/data.xml'
    ],

    "active": False,
    "installable": True,
    'application': False,
}
