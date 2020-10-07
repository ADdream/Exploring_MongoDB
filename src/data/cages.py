import mongoengine
import datetime
from data.bookings import Booking

class Cage(mongoengine.Document):

    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    cost = mongoengine.FloatField(required=True)
    square_meters = mongoengine.FloatField(required=True)
    is_carpented = mongoengine.BooleanField(requried=True)
    has_toys = mongoengine.BooleanField(required=True)
    allow_dangerous_snakes = mongoengine.BooleanField(required=True)

    bookings = mongoengine.EmbeddedDocumentListField(Booking)

    meta = {
        'db_alias': 'core',
        'collection': 'cages'

    }


