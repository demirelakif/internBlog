from mongoengine import *
import datetime
import pytz
from pytz import timezone

class User(Document):
    name = StringField()
    surname=StringField()
    username = StringField(Required=True,unique=True)
    password = StringField(Required=True)
    email = EmailField()
    author = BooleanField(default=False)
    utc_now = datetime.datetime.utcnow()
    utc = pytz.timezone('UTC')
    aware_date = utc.localize(utc_now)
    turkey = timezone('Europe/Istanbul')
    date_modified = DateTimeField(default=aware_date.astimezone(turkey))


class Article(Document):
    user_id = IntField(Required=True)
    title = StringField(Required=True)
    author = StringField(Required=True)
    description = StringField(Required=True)
    vote = IntField(default=0)
    upvotes = ListField(StringField())
    downvotes = ListField(StringField())
    
