from flask import Flask
import json

animals = ["Tiger", "Lion", "Monkey", "Owl", "Snake", "Mouse", "Eagle"]

app = Flask (__name__)

@app.get('/animals')
def get_animal():
    return "Tiger, Lion, Monkey, Owl, Snake, Mouse, Eagle"

@app.post('/animals')
def add_animal():
    return "Elephant"

@app.patch('/animals')
def edit_animal():
    return "Panther"

@app.delete('/animals')
def delete_animal():
    return "Animal"

app.run(debug = True)