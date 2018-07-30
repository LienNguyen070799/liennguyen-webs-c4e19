from models.service import Service

import mlab
from faker import Faker
from random import randint,choice
fake = Faker()
mlab.connect()
# print(fake.name(),fake.address())
for i in range(50) :
    print( "saving....", i+1)
    new_service = Service(
        name = fake.name(),
        yob = randint(1990,2000),
        gender = randint(0,1),
        height = randint(150,190),
        phone = fake.phone_number(),
        address = fake.address(),
        status = choice([True,False])
    )
    new_service.save()