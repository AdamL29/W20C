from flask import Flask, request
import json
from dbhelpers import run_statement

animals = ["Tiger", "Lion", "Monkey", "Owl", "Snake", "Mouse", "Eagle"]

app = Flask (__name__)

@app.get('/animals')
def get_animal():
    result = run_statement("CALL get_animal")
    if (type(result) == list):
        result_json = json.dumps(result)
        return result_json
        # Short term is = return json.dumps(result)
    else:
        return "Sorry, something went wrong."

@app.post('/animals')
def add_animal():
    animal_name = request.json.get('animalName')
    if animal_name == None:
        return "You must specify an animalName."
    result = run_statement("CALL add_animal(?)", [animal_name])
    if result == None:
        return "Success!!"
    else:
        return "Something went terribly wrong."

@app.patch('/animals')
def edit_animal():
    animal_update = request.json.get('animalUpdate')
    if animal_update == None:
        return "You must specify an authorName."
    result = run_statement("CALL edit_animal(?)", [animal_update])
    if result == None:
        return "Success?!"
    else:
        return "Something went terribly wrong."

@app.delete('/animals')
def delete_animal():
    animal_id = request.json.get('animalId')
    if animal_id == None:
        return "You must specify an animalIde."
    result = run_statement("CALL delete_animal(?)", [animal_id])
    if result == None:
        return "Success!"
    else:
        return "Something went terribly wrong."

app.run(debug = True)