from render_engine import Site, Page, Collection, Blog

site = Site(strict=True)
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
        }

class Product(Page):
    list_attrs = ['certifications', 'ppe']

@site.register_collection
class products(Collection):
    page_content_type = Product
    template = 'products.html'
    routes = ["", "products"]
    subcollections = ['category']
    content_path = "content"
    has_archive = True
    archive_slug = 'all_products.html'
    archive_template = "all_products.html"

    @staticmethod
    def archive_default_sort(cls):
        return (cls.product_description)

@site.register_collection
class dispensers(Collection):
    routes = ["", "dispensers"] # routes will appear at '/page' and '/pages/page'
    content_path = "content/dispensers" # collections must have their paths assigned
    has_archive = True
    archive_template = "all_dispensers.html"
    archive_slug = 'all_dispensers.html'
    template = 'dispensers.html'

class Index(Page):
    template = "index.html" # page.html is the default template but you can make a custom template
    slug = "index"
    content_path = 'content/pages/index.md'

    def __init__(self):
        super().__init__()
        self.dispensers = site.collections['dispensers'].pages
        self.hide_header = True

site.route(Index())
site.render()
