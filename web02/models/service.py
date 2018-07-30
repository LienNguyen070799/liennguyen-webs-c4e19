from mongoengine import *
class Service(Document) :
    name = StringField()
    yob = IntField()
    gender =  IntField()
    height =  IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()

# new_service = Service(
#     name = "Boss",
#     yob = 2000,
#     gender = 0,
#     height = 150,
#     phone = "000000000",
#     address = "Dong Anh, Hanoi",
#     status = False
# )


# new_service.save()