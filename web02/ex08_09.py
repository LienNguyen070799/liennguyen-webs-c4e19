from mongoengine import *
import ex07
ex07.connect()
class river(Document):
    name = StringField()
    continent = StringField()
    length = IntField()
# ex08
river_africa = river.objects(continent = 'Africa')
for i in range(len(river_africa)):
    print(river_africa[i].name,end = ', ')
print()
# ex09
river = river.objects(continent = 'S. America',length__lte = 1000)
for i in range(len(river)):
    print(river[i].name,end = ', ')