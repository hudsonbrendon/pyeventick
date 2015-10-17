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
            self.__token = requests.get(self.get_url_api('tokens.json'), auth=HTTPBasicAuth(self.email, self.password)).json()
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

    def events(self):
        '''Return a json with list of events'''
        try:
            request = requests.get(self.get_url_api('events.json'), auth=self.get_token()).json()
        except:
            raise ConectionError('Connection failed!')
        return request

    def event(self, event_id):
        '''Returns a json with iformations of a event'''
        try:
            request = requests.get(self.get_url_api('events/{}.json').format(event_id), auth=self.get_token()).json()
        except:
            raise ConectionError('Connection failed!')
        return request

    def attendees(self, event_id, checked_after):
        '''Returns a json with all participants of an event'''
        try:
            request = requests.get(self.get_url_api('events/{}/attendees.json?checked_after={}').format(event_id, checked_after), auth=self.get_token()).json()
        except:
            raise ConectionError('Connection failed!')
        return request

    def attendee(self, event_id, ID):
        '''Returns a json with the information of a participant of the event'''
        try:
            request = requests.get(self.get_url_api('events/{}/attendees/{}.json').format(event_id, ID), auth=self.get_token()).json()
        except:
            raise ConectionError('Connection failed!')
        return request
