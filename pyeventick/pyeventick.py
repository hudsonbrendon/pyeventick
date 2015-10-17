# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
from exception import ConectionError, AuthenticationError


URL = 'https://www.eventick.com.br/api/v1/'

class Eventick(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password

        try:
            self.__token = requests.get(URL + 'tokens.json', auth=HTTPBasicAuth(self.email, self.password)).json()
        except:
            raise AuthenticationError('Authentication failed!')

    def get_token(self):
        '''Return token or credentials'''
        if self.__token:
            return (self.__token.values()[0], '')
        else:
            return (self.email, self.password)

    def get_url_api(self, url):
        '''Return api url'''
        return URL + '{}'.format(url)
