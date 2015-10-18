# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
from exception import ConectionError, AuthenticationError
from datetime import datetime
import json

URL = 'https://www.eventick.com.br/api/v1/'

class Eventick(object):
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

        try:
            self.__token = requests.get(self.get_api_url('tokens.json'), auth=HTTPBasicAuth(self.__email, self.__password)).json()
        except:
            raise AuthenticationError('Authentication failed!')

    def get_token(self):
        '''Return a token or credentials'''
        if self.__token:
            return (self.__token.values()[0], '')
        else:
            return (self.email, self.password)

    def get_api_url(self, url):
        '''Returns a json with the list of events'''
        return URL + '{}'.format(url)

    def events(self):
        '''Returns a json with the list of events'''
        try:
            request = requests.get(self.get_api_url('events.json'), auth=self.get_token()).json()
        except:
            raise ConectionError('Connection failed!')
        return request

    def event(self, event_id):
        '''Returns a json with iformations of a event'''
        try:
            request = requests.get(self.get_api_url('events/{}.json').format(event_id), auth=self.get_token()).json()
        except:
            raise ConectionError('Connection failed!')
        return request

    def attendees(self, event_id, checked_after=None):
        '''Returns a json with all participants of an event'''
        try:
            if checked_after is None:
                checked_after = datetime.now()
                checked_after = checked_after.strftime('%Y-%m-%dT%H:%M:%S-03:00')
            request = requests.get(self.get_api_url('events/{}/attendees.json?checked_after={}').format(event_id, checked_after), auth=self.get_token()).json()
        except:
            raise ConectionError('Connection failed!')
        return request

    def attendee(self, event_id, ID):
        '''Returns a json with the information of a participant of the event'''
        try:
            request = requests.get(self.get_api_url('events/{}/attendees/{}.json').format(event_id, ID), auth=self.get_token()).json()
        except:
            raise ConectionError('Connection failed!')
        return request

    def checkin(self, event_id, code, checked_at):
        ''''''
        try:
            request = requests.put(self.get_api_url('events/{}/attendees/{}.json?checked_at={}').format(event_id, code, checked_at), auth=self.get_token())
        except:
            raise ConectionError('Connection failed!')
        return request.status_code

    def checkin_all(self, event_id, attendees):
        ''''''
        try:
            request = requests.put(self.get_api_url('events/{}/attendees/check_all.json').format(event_id), auth=self.get_token(), data=json.dumps(attendees), headers={'Content-Type': 'application/json'})
        except:
            raise ConectionError('Connection failed!')
        return request.status_code
