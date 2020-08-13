from render_engine import Site
from dataclasses import dataclass


site = Site()
site.SOLSTA_CATEGORIES = {
        '100': 'Cleaners/Degreasers',
        '200': 'All-Purpose Cleaners',
        '300': 'Restroom Cleaners',
        '400': 'Multi-Use Cleaners',
        '500': 'Glass & Surface Cleaner',
        '600': 'Air Fresheners',
        '700': 'Hard Surface Disinfectant Cleaners',
        '800': 'Carpet Cleaners',
        '900': 'FoodService Cleaners/Sanitizer',
        }

site.tools = {
        'face shield': '/static/shutter_shield.png',
        'apron': '/static/shutter_apron.png',
        'gloves': '/static/shutter_gloves.png',
        'safety glasses': '/static/shutter_glasses.png',
        'wet floor sign': '/static/shutter_sign.png',
        }

site.CERTIFICATIONS = {
        'ul 2759': {
            'description': '<p>PRODUCT CERTIFIED FOR REDUCED ENVIRONMENTAL \
            IMPACT. \
            VIEW SPECIFIC ATTRIBUTES EVALUATED UL.COM/EL</p><p>UL 2759</p>',
            'image': '/static/ecologo.jpg',
            },
        'cacc': {
            'description': 'This product has been granted a CACC certificate by the South Coast AQMD',
            'link': "http://www.aqmd.gov/home/programs/business/business-detail?title=cacc-cert&parent=certification-programs-training",
            'image': '/static/cacc.jpg',
            },
        'epa': {
            'description': 'Formulated in Parternship with EPA DfE'
            },
        'cri': {
            'description': 'CRI Seal of Approval'
            },
        'gs-37': {
            'description': 'Green Seal Certified: GS-37',
            },
        }
site.strict = True
