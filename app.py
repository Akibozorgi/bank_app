from flask import Flask,render_template, request, jsonify
from repository.database_maker import create_database
from controller.person_controller import PersonController

app = Flask(__name__)

# create_database()

@app.route('/')
def home():
    person_controller = PersonController()
    status, person_list = person_controller.find_all()
    print(person_list)
    return render_template("person.html",person_list=person_list)

@app.route('/api/persons')
def persons():
    # person_controller = PersonController()
    # status, person_list = person_controller.find_all()
    return [{"id": 1, "name": "api-test", "family":"alipour"},{"id": 2, "name": "reza", "family":"rezaii"}]

@app.route('/persons', methods=['POST'])
def save_person():
    name = request.form.get('name')
    family = request.form.get('family')
    birth_date = request.form.get('birth_date')
    username = request.form.get('username')
    password = request.form.get('password')
    person_controller = PersonController()
    status, message =  person_controller.save(name,family,birth_date,username,password)
    print(message)
    status, person_list = person_controller.find_all()
    return render_template("person.html",person_list=person_list, status=status, message=message)

app.run(host="192.168.39.100", port=80, debug=True)
