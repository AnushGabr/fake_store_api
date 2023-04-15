import json

from base.base_api import BaseApi


class ProductService(BaseApi):
    products_endpoint = '/products'
    category_endpoint = "/products/category/jewelery"
    def get_products(self, url, token):
        response = self.get_request(url + self.products_endpoint)

        return response

    def get_products_by_category(self, url):
        endpoint = self.category_endpoint
        response = self.get_request(url + endpoint)
        return response

    def create_new_product(self, url, json):
        response = self.post_request(url + self.products_endpoint, json)
        #self.check_status_code(response, 201)
        return response

    def check_products_data_by_length(self, data):
        json_data = json.loads(data.text)

        return len(json_data)

    def update_product(self, url, product_id, json_for_update, headers):
        """

        :param url: The base url for making the request.
        :param product_id: The product id number that we what to update.
        :param json_for_update: The new product details that we want to update.
        :param headers: The headers that must have two keys; Host and Authorization.
        :return: Returns the response.
        """
        response = self.put_request(url+self.products_endpoint+"/"+str(product_id), json_for_update, headers)
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
        response = self.delete_request(url+self.products_endpoint+"/"+str(product_id), headers)
        return response
