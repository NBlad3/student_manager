from app.models import Dog, Cat
from flask import request, jsonify
from app import app, db

@app.route("/view-<species>", methods=["GET"])
def view(species):

    pets = []

    dogs = Dog.query.all()
    cats = Cat.query.all()


    if species == "dogs":
        for dog in dogs:
            dog = dog.__dict__
            del dog["_sa_instance_state"]
            pets.append(dog)

    elif species == "cats":
        for cat in cats:
            cat = cat.__dict__
            del cat["_sa_instance_state"]
            pets.append(cat)

    else:
        return jsonify({"message": "You can only view cats and dogs"}), 400

    return jsonify({"response": pets, "message": "Successful"}), 200




@app.route("/add-<species>", methods=["POST"])
def add(species):

    data = request.get_json()
    name = data["name"]
    age = data["age"]

    if name is None or name == "":
        name = None

    if age is None or age == "":
        age = None


    if species == "dog":
        new_dog = Dog(name=name, age=age)
        db.session.add(new_dog)
        db.session.commit()
    elif species == "cat":
        new_cat = Cat(name=name, age=age)  # Changed from Dog to Cat
        db.session.add(new_cat)
        db.session.commit()
    else:
        return jsonify({"message": "You can only add cats and dogs"}), 400

    return jsonify({"message": "Successful"}), 200



@app.route("/edit-<species>", methods = ["PUT"])
def edit(species):

    data = request.get_json()
    pet_id = data["id"]


    if species == "dog":
        dog = Dog.query.filter_by(id=pet_id).first()
        if "new_name" in data:
            dog.name = data["new_name"]
        if "new_age" in data:
            dog.age = data["new_age"]

    elif species == "cat":
        cat = Cat.query.filter_by(id=pet_id).first()
        if "new_name" in data:
            cat.name = data["new_name"]
        if "new_age" in data:
            cat.age = data["new_age"]

    else:
        return jsonify({"message": "You can only edit cats and dogs"}), 400

    db.session.commit()

    return jsonify({"message": "Successful"})


@app.route("/delete-<species>", methods=["DELETE"])
def delete(species):
    data = request.get_json()
    pet_id = data.get("id")

    if species == "dog":
        dog = Dog.query.filter_by(id=pet_id).first()
        db.session.delete(dog)

    elif species == "cat":
        cat = Cat.query.filter_by(id=pet_id).first()
        db.session.delete(cat)

    else:
        return jsonify({"message": "You can only delete cats and dogs"}), 400

    db.session.commit()

    return jsonify({"message": "Successful"}), 200

    

