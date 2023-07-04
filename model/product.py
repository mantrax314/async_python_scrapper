from datetime import datetime


class Product:

    def __init__(self, product_id, url, name, price, scrap_field, created_at, updated_at):
        self.product_id = product_id
        self.url = url
        self.name = name
        self.price = float(price)
        self.scrap_field = scrap_field
        self.created_at = created_at
        self.updated_at = updated_at

    def return_as_map(self):

        if type(self.created_at) is datetime:
            self.created_at = self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        if type(self.updated_at) is datetime:
            self.updated_at = self.updated_at.strftime('%Y-%m-%d %H:%M:%S')

        return {"product_id": self.product_id, "url": self.url, "name": self.name, "price": self.price,
                "scrap_field": self.scrap_field, "created_at": self.created_at, "updated_at": self.updated_at}
