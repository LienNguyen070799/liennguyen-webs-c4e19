# query la truy van
from models.service import Service
import mlab

mlab.connect()


id_to_find = "5b5b1dc6e6b9c96210b2f2e0"
# service = Service.objects( id = id_to_find)
# print (service)
# service = Service.objects.get( id = id_to_find) #=> list
# print(service)
service = Service.objects.with_id(id_to_find)
#nên dùng with_id
# print(service.to_mongo())

# delete
if service is not None:

    # service.delete()
    # print(" Deleted")

    # update
    print(service.to_mongo())
    service.update(set__name = "linh", set__gender = 1)
    service.reload()
    print(service.to_mongo())

else:
    print(" Not found")

# all_service = Service.objects()

# first_service = all_service[0]

# print(first_service['yob'],a)
