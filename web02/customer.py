from mongoengine import *
import mlab
from faker import Faker
from random import randint,choice
fake = Faker()
mlab.connect()
class Customer (Document) :
    name = StringField()
    gender =  IntField()
    email = EmailField()
    phone_number = StringField()
    job = StringField()
    company = StringField()
    connected = BooleanField()
for i in range (35) :
    new_customer = Customer(
        name = fake.name(),
        gender = randint(0,1),
        email = fake.email(),
        phone_number = fake.phone_number(),
        job = fake.job(),
        company = fake.company(),
        connected = choice([True, False])
    )
    new_customer.save()

   