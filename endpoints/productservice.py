from base.base_api import BaseApi


class ProductService(BaseApi):
    products_endpoint = '/products'

    def get_products(self, url, token, expected_status_code):
        response = self.get_request(url + self.products_endpoint, token)

        return self.check_status_code(response, expected_status_code)
