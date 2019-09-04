from eventbrite import Eventbrite
from social_django.models import UserSocialAuth


def get_auth_token(user):
    try:
        token = user.social_auth.get(
            provider='eventbrite'
        ).access_token
    except UserSocialAuth.DoesNotExist:
        return ''
    return token


def get_api_events(token):
    eventbrite = Eventbrite(token)
    return eventbrite.get('/users/me/events/?page_size=10')


def get_api_event_id(token, event_id):
    eventbrite = Eventbrite(token)
    return eventbrite.get('/events/{}'.format(event_id))
