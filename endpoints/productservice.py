import json

from base.base_api import BaseApi


class ProductService(BaseApi):
    PRODUCTS_ENDPOINT = '/products'
    sorted_product_endpoint_desc = '/products?sort=desc'
    sorted_product_endpoint_asc = '/products?sort=asc'
    all_categories_endpoint = '/products/categories'

    def get_products(self, url, token):
        response = self.get_request(url + self.PRODUCTS_ENDPOINT, token)

        return response

    def create_product(self, url, json, token):
        response = self.post_request(url + self.PRODUCTS_ENDPOINT, json, token)

        return response

    def get_single_product(self, url, token, id):
        response = self.get_request(url + self.PRODUCTS_ENDPOINT + id, token)
        product = response.json()

        return product["id"]

    def get_limit_results(self, url, token, id):
        products_ids = []
        response = self.get_request(url + self.PRODUCTS_ENDPOINT + id, token)
        limited_products = response.json()
        for product in limited_products:
            products_ids.append(product["id"])

        return products_ids

    def check_products_data_by_length(self, data):
        json_data = json.loads(data.text)

        return len(json_data)

    def create_new_product(self, url, json, token):
        response = self.post_request(url + self.PRODUCTS_ENDPOINT, json, token)

        return response

    def update_product(self, url, product_id, json_for_update, headers):
        """

        :param url: The base url for making the request.
        :param product_id: The product id number that we what to update.
        :param json_for_update: The new product details that we want to update.
        :param headers: The headers that must have two keys; Host and Authorization.
        :return: Returns the response.
        """
        response = self.put_request(url + self.PRODUCTS_ENDPOINT + "/" + str(product_id), json_for_update, headers)
        return response

    def check_response_body_key(self, response, json_for_update, key):
        """

        :param response: The response that we want to check.
        :param json_for_update: The new product details that we updated.
        :param key: The json/dict key through which we want to check the response body.
        :return: Return True is the key is updated.
        """
        updated_json = json.loads(response.text)
        return str(json_for_update[key]) == updated_json[key]  # str() is used in order to compare int to str.

    def is_product_entirely_updated(self, response, json_for_update):
        """

        :param response: The response that we want to check.
        :param json_for_update: The new product details that we updated.
        :return: Returns True if all the product details were updated correctly.
        """
        updated_json = json.loads(response.text)
        return all(updated_json[key] == str(json_for_update[key]) for key in list(json_for_update.keys()))

    def update_single_data(self, url, json_for_update):
        pass  # This one is for patch request

    def delete_product(self, url, product_id, headers):
        """

        :param url: The base url for making the request.
        :param product_id: The product id number that we want to delete.
        :param headers: The headers that must have two keys; Host and Authorization.
        :return: Returns the response.
        """
        response = self.delete_request(url + self.PRODUCTS_ENDPOINT + "/" + str(product_id), headers)
        return response




    def sort_by_descending(self, url, token):
        ides = []
        response = self.get_request(url + self.sorted_product_endpoint_desc, token)
        products = response.json()
        for product in products:
            ides.append(product["id"])

        sorted_ides = sorted(ides, reverse=True)
        return sorted_ides == ides


    def sort_by_ascending(self, url, token):
        ides = []
        response = self.get_request(url + self.sorted_product_endpoint_asc, token)
        products = response.json()
        for product in products:
            ides.append(product["id"])

        sorted_prices = sorted(ides)
        return sorted_prices



    def get_all_requests(self, url, token):
        request = self.get_request(url + self.all_categories_endpoint, token)
        categories = request.json()
        return len(categories) == 4
