from app.models import Student
from flask import request, jsonify
from app import app, db

@app.route("/view", methods=["GET"])
def view():

    response = []
    students = Student.query.all()

    for student in students:
        student = student.__dict__
        del student["_sa_instance_state"]
        response.append(student)

    return jsonify({"response": response, "message": "Successful"}), 200


@app.route("/add", methods=["POST"])
def add():

    data = request.get_json()
    name = data["name"]
    age = data["age"]
    email = data["email"]

    new_student = Student(name=name, age=age, email=email)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Successful"}), 200


'''@app.route("/edit", methods = ["PUT"])
def edit():

    data = request.get_json()
    student_id = data["id"]



        dog = Dog.query.filter_by(id=pet_id).first()
        if "new_name" in data:
            dog.name = data["new_name"]
        if "new_age" in data:
            dog.age = data["new_age"]





    db.session.commit()

    return jsonify({"message": "Successful"})


@app.route("/delete", methods=["DELETE"])
def delete():
    data = request.get_json()
    pet_id = data.get("id")


        dog = Dog.query.filter_by(id=pet_id).first()
        db.session.delete(dog)




    return jsonify({"message": "Successful"}), 200'''


    

