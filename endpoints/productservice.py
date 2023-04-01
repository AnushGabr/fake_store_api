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







