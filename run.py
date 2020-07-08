from render_engine import Page, Collection, Blog
from app import site

class Product(Page):
    list_attrs = ['certifications', 'ppe']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if hasattr(self, 'certifications'):
            self.certifications = sorted(self.certifications, key=lambda x:x)
            print(self.certifications)

        if hasattr(self, 'ppe'):
            self.ppe = sorted(self.ppe, key=lambda x:x)
            print(self.ppe)

@site.register_collection
class Products(Collection):
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
class Dispensers(Collection):
    routes = ["", "dispensers"] # routes will appear at '/page' and '/pages/page'
    content_path = "content/dispensers" # collections must have their paths assigned
    has_archive = True
    archive_template = "all_dispensers.html"
    archive_slug = 'all_dispensers.html'
    template = 'dispensers.html'


@site.register_collection
class Accessories(Collection):
    content_path = "content/accessories"
    routes = ["accessories"]
    has_archive = True

class Index(Page):
    template = "index.html" # page.html is the default template but you can make a custom template
    slug = "index"
    content_path = 'content/pages/index.md'

    def __init__(self):
        super().__init__()
        self.dispensers = site.collections['Dispensers'].pages
        self.hide_header = True

site.route(Index())
site.render()
