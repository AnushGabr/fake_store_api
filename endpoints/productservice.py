import json

from base.base_api import BaseApi


class ProductService(BaseApi):
    products_endpoint = '/products'

    def get_products(self, url, token):
        response = self.get_request(url + self.products_endpoint, token)

        return response

    def check_products_data_by_length(self, data):
        json_data = json.loads(data.text)

        return len(json_data)

    #checking
    def update_product(self, url, token, id):
        response = self.put_request(url + self.products_endpoint, {"title": "test product",
    "price": 13.5,},token, id)


