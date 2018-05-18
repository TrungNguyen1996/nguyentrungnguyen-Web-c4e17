from models.service import Service
import mlab

mlab.connect()

id_to_find = "5af5a13948e64310045b8511"

# hera = Service.object(id=id_to_find) # Hera  dạng list có phần tử id
# hera = Service.oblject.get(id=id_to_find) # Hera là một chuổi id luôn/hera là một dictional chứa
hera = Service.objects.with_id(id_to_find) # giống cách get id

if hera is not None:
    # hera.delete()
    print()
    hera.update(set__address="Trần Duy Hưng", set__height=173)
    # hera.reload()
    print(hera.address)
    # print("Delete")
else:
    print("Service not found")



# print(hera.to_mongo())
hera.delete() # có ID đã tìm đc rồi mới xóa






# all_service = Service.objects(gender=1) #  lấy tất cả

# first_service = all_service[0]

# for index, service in enumerate(all_service):
#     print(service['name'])
#     if index == 9:
#         break

# server = Service.objects.get (id= '5af59bef48e6430c20ed29d8')
