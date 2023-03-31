import requests


class BaseApi:

    def get_request(self, url, headers, params=None):
        """
        Use this method to send the get request
        :param url: The request URL
        :param params: The request params(OPTIONAL)
        :param headers: The request headers(OPTIONAL)
        :return: response
        """
        response = requests.get(url, headers=headers, params=params, verify=False)
        return response

    def post_request(self, url, json, headers, params=None):
        """
        Use this method to send post request
        :param url: The request URL
        :param json: Request body format
        :param params: The request params(OPTIONAL)
        :param headers: The request headers(OPTIONAL)
        :return: response
        """

        response = requests.post(url, data=json, params=params, headers=headers, verify=False)
        return response

    def put_request(self, url, json, *kwargs):

        """"
        Use this method to send put request
        :param url: The request URL
        :param json: Request body format
        :param params: The request params(OPTIONAL)
        :param headers: The request headers(OPTIONAL)
        :return: response
        """

        response = requests.put(url, json, params=kwargs[1], headers=kwargs[0], verify=False)
        return response

    def delete_request(self, url, *kwargs):
        """
        Use this method to send delete request
        :param url: The request URL
        :param params: The request params(OPTIONAL)
        :param headers: The request headers(OPTIONAL)
        :return: response
        """
        response = requests.delete(url, headers=kwargs[0], verify=False)
        return response

    def check_status_code(self, response, expected_status_code):
        """
        Use this method to check response status code
        :param response:
        :param expected_status_code:
        :return:
        """

        return response.status_code == expected_status_code




