from render_engine import Page, Collection, Blog
from app import site

class Product(Page):
    list_attrs = ['certifications', 'ppe']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if hasattr(self, 'certifications'):
            self.certifications = sorted(self.certifications, key=lambda x:x)

        if hasattr(self, 'ppe'):
            self.ppe = sorted(self.ppe, key=lambda x:x)

class Products(Collection):
    @staticmethod
    def archive_default_sort(cls):
        return (cls.waxie_item_number)

@site.register_collection
class Chemicals(Products):
    page_content_type = Product
    template = 'products.html'
    routes = ["", "products"]
    subcollections = ['category']
    content_path = "content"
    has_archive = True
    archive_slug = 'all_products.html'
    archive_template = "all_products.html"


@site.register_collection
class Dispensers(Products):
    routes = ["", "dispensers"] # routes will appear at '/page' and '/pages/page'
    content_path = "content/dispensers" # collections must have their paths assigned
    has_archive = True
    archive_template = "all_dispensers.html"
    archive_slug = 'all_dispensers.html'
    template = 'dispensers.html'


@site.register_collection
class Accessories(Products):
    page_content_type = Product
    content_path = "content/accessories"
    routes = ["", "accessories"]
    has_archive = True
    template = 'products.html'
    archive_slug = 'all_accessories'
    archive_template = "all_accessories.html"


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
