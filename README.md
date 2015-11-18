# Pyeventick

![Logo](logo.png)

Simple integrate of eventick.com.br API  with Python

# Quick start

```bash
$ pip install pyeventick
```
or

```bash
$ python setup.py install
```
# Usage

To access the API you`ll need to login, use:

```python
>>> from pyeventick import Eventick

>>> eventick = Eventick('email@email.com','password')
```

## Events
To list all the events, use:  
```python
>>> eventick.events()
```
This returns a dictionary of all the events.

```python
{
  u'events': [
      {
        u'theme_color': u'7cb342',
        u'thumbnail_url': u'https://dien0bhzxjun5.cloudfront.net/5d9239c5-8a54-482a-86e8-e4dab34c43c8/logo.crop_656x242_0,53.scale_crop_357x107.jpg',
        u'start_at': u'2015-10-21 13:00:00 -0200',
        u'id': 20585,
        u'title': u'Event Test'
      }
    ]
}
```
## Event

To get the data of just one event, use:
```python
>>> eventick.event(20585)
```
It returns a dictionary with information from an event.
```python
{
  u'events': [
      {
        u'theme_color': u'7cb342',
        u'thumbnail_url': u'https://dien0bhzxjun5.cloudfront.net/5d9239c5-8a54-482a-86e8-e4dab34c43c8/logo.crop_656x242_0,53.scale_crop_357x107.jpg',
        u'start_at': u'2015-10-21 13:00:00 -0200',
        u'id': 20585,
        u'title': u'Event Test'
      }
    ]
}
```
## Attendees
To list all the attendees, use:
```python
>>> eventick.attendees(20585, '2015-09-10 16:00:00 -0300')
```
It returns a dictionary with all the attendees information.

```python
{
  u'attendees':
    [
      {
        u'code': u'NWJ2MXZN',
        u'name': u'Attendee 1',
        u'ticket_type': u'Gratuito'.,
        u'id': 874921,
        u'checked_at':u'2015-09-10 16:00:00 -0300',
        u'email': u'email@email.com'
      },
      {
        u'code': u'XS40UGTT',
        u'name': u'Attendee 2',
        u'ticket_type': u'Gratuito',
        u'id': 874928,
        u'checked_at': u'2015-09-10 16:00:00 -0300',
        u'email': u'email@email.com'
      },
      {
        u'code': u'IASUP7DU',
        u'name': u'Attendee 3',
        u'ticket_type': u'Gratuito',
        u'id': 873326,
        u'checked_at': u'2015-09-10 16:00:00 -0300',
        u'email': u'email@email.com'
      }
    ]
}
```

## Attendee

To get data from just one specific event/attendee:

```python
>>> eventick.attendee(20585, 874921)
```
It returns a dictionary with information from one attendee.

```python
{
  u'attendees':
    [
      {
        u'code': u'NWJ2MXZN',
        u'name': u'Attendee 1',
        u'ticket_type': u'Gratuito',
        u'id': 874921,
        u'checked_at':u'2015-09-10 16:00:00 -0300',
        u'email': u'email@email.com'
      }
    ]
}
```
## Check-in
To check in a participant use:
```python
>>> eventick.checkin(12345, 'XXXXXXXX', '2015-10-17T16:54:35-03:00')
```
It returns a 200 code.

## Check-in all
To check in multiple participants use:
```python
>>> eventick.checkin_all(21091, {"attendees":[{"id":12345,"checked_at":"2015-10-17T16:54:35-03:00"}, {"id":67890,"checked_at":"2015-10-17T16:54:35-03:00"}]})
```
It returns a 200 code.

# Dependencies
- Python 2.7
- [requests](http://docs.python-requests.org/en/latest/)

# License
[MIT](http://en.wikipedia.org/wiki/MIT_License)
