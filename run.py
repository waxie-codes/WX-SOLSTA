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

@site.register_route
class Index(Page):
    template = "index.html" # page.html is the default template but you can make a custom template
    slug = "index"
    content_path = 'content/pages/index.md'


@site.register_collection
class products(Collection):
    routes = ["", "products"]
    content_path = "content"
    has_archive = True
    archive_slug = 'all_products.html'
    archive_template = "all_products.html"
    template = 'products.html'


@site.register_collection
class dispensers(Collection):
    routes = ["", "dispensers"] # routes will appear at '/page' and '/pages/page'
    content_path = "content/dispensers" # collections must have their paths assigned
    has_archive = True
    archive_template = "all_dispensers.html"
    archive_slug = 'all_dispensers.html'
    template = 'dispensers.html'

site.render()
