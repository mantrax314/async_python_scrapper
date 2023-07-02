class Product:

    def __init__(self, product_id, url, name, price, scrap_field, created_at, updated_at):
        self.product_id = product_id
        self.url = url
        self.name = name
        self.price = float(price)
        self.scrap_field = scrap_field
        self.created_at = created_at
        self.updated_at = updated_at
