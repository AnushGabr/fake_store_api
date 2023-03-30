import requests


class BaseApi:

    def get_request(self, url, params=None, headers=None):
        """
        Use this method to send the get request
        :param url: The request URL
        :param params: The request params(OPTIONAL)
        :param headers: The request headers(OPTIONAL)
        :return: response
        """
        response = requests.get(url, headers=headers, params=params, verify=False)
        return response

    def check_status_code(self, response, expected_status_code):
        """
        Use this method to check response status code
        :param response:
        :param expected_status_code:
        :return:
        """

        return response.status_code == expected_status_code
