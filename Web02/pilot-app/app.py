
from flask import * #Flask, render_template, redirect, url_for
from mongoengine import *
from models.service import Service

import mlab

app = Flask(__name__)

mlab.connect()

# # design database
# # crate collection
# class Service(Document):
#     name = StringField()
#     yob = IntField()
#     gender = IntField()
#     height = IntField()
#     phone = StringField()
#     address = StringField()
#     status = BooleanField()



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def seach(g):
    all_service = Service.objects(gender = g, yob__lte = 2000, address__contains = "Hà Nội") # Service là class chứa data
    return render_template('search.html', all_service=all_service)

@app.route('/admin')
def admin():
    all_services = Service.objects()
    # service = all_service[0]
    return render_template('admin.html', all_services=all_services)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('admin'))
    else:
        return "Service"

@app.route('/new-service', methods=['GET','POST'])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form

        name = form['name']
        yob = form['yob']

        new_service = Service(name=name, yob=yob)
        new_service.save()

        return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
