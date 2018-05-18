from mlab import connect
from models.service import Service

# 1. Connect
connect()

# 2. Find By Id
id = "5af5a08248e6430c0840e9ec"
service = Service.objects.with_id(id)
print(service.name)

# 3. Delete
service.delete()
print("Done")

# 4. 
