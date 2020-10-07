import mongoengine


class Booking(mongoengine.EmbeddedDocument):
    guest_owner_id = mongoengine.ObjectIdField()
    guest_snake_id = mongoengine.ObjectIdField()

    booked_date = mongoengine.DateTimeField()
    checkin_date = mongoengine.DateTimeField(required=True)
    chckout_date = mongoengine.DateTimeField(required=True)

    review = mongoengine.StringField()
    rating = mongoengine.IntField(default=0)

    @property
    def duration_in_days(self):
        dt_diff = self.chckout_date - self.checkin_date
        return dt_diff.days




