import requests


class BaseApi:

    def get_request(self, url, headers=None, params=None):
        """
        Use this method to send the get request
        :param url: The request URL
        :param headers: The request params(OPTIONAL)
        :param params: The request headers(OPTIONAL)
        :return: response
        """
        response = requests.get(url, headers=headers, params=params)
        return response

    def post_request(self, url, json, headers=None, params=None):
        """
        Use this method to send post request
        :param url: The request URL
        :param json: Request body format
        :param headers: The request headers(OPTIONAL)
        :param params: The request params(OPTIONAL)
        :return: response
        """

        response = requests.post(url, data=json, params=params, headers=headers, verify=False)
        return response

    def put_request(self, url, json, headers=None, params=None):

        """"
        Use this method to send put request
        :param url: The request URL
        :param json: Request body format
        :param headers: The request params(OPTIONAL)
        :param params: The request headers(OPTIONAL)
        :return: response
        """

        response = requests.put(url, json, headers=headers, params=params, verify=False)
        return response

    def patch_request(self, url, json, headers=None, params=None):
        """

        :param url: The request URL
        :param json: Request body format
        :param headers: The request params(OPTIONAL)
        :param params: The request headers(OPTIONAL)
        :return: response
        """
        response = requests.patch(url, json, headers=headers, params=params, verify=False)
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
        :param response: The response that we want to check.
        :param expected_status_code: The expected status code for the requests we made.
        :return: Returns True if the actual status code matches the expected one.
        """

        return response.status_code == expected_status_code

    def get_auth_headers(self, host, access_token):
        """

        :param host: The host name and port for the request. If the port is not specified the default port is used.
        :param access_token: The token that was received after logging in into the system with valid login and pass.
        :return: Returns a dictionary with the most important header keys and their values.
        """
        headers = {
            "Host": host[8:],
            'Authorization': f'Bearer {access_token}'
        }
        return headers

    def check_response_time_in_seconds(self, response, maximum_expected_time):
        """

        :param response: The response that we want to check.
        :param maximum_expected_time: The maximum seconds that the server can send a response to the requests.
        :return: Returns True if our expected maximum seconds is not passed.
        """
        actual_response_time = response.elapsed.total_seconds()
        return actual_response_time < float(maximum_expected_time)
