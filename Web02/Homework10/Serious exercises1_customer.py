from mongoengine import Document, StringField, IntField, BooleanField

class Customer(Document): # Customer kế thừa thừ Document
    name=StringField()
    email=StringField()
    contacted=BooleanField()
    gender=BooleanField()
    phone=StringField()
    job=StringField()
    company=StringField()
    contacted=StringField()

# 2. Use faker
import mlab

app = Flask(__name__)

mlab.connect()
# 3. save

# 4. Flask
