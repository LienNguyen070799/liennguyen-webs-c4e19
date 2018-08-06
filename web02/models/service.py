from mongoengine import *
import mlab
mlab.connect()
class Service(Document) :
    image = ImageField()
    name = StringField()
    yob = IntField()
    gender =  IntField()
    height =  IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    description = StringField()
    measurements = ListField(IntField())
    

new_service = Service(
    
    name = "Trâm Anh",
    yob = 1998,
    gender = 0,
    height = 165,
    phone = "000000000",
    address = "Hà Nội",
    status = False,
    description = 'Ngoan,hiền, dễ thương, lễ phép với gia đình,...',
    measurements = [90,60,90]
)
new_service.save()