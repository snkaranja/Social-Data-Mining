from app import app
from flask import Flask, request, render_template, url_for,jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_mongoengine import MongoEngine

app = Flask(__name__)  
client = MongoClient("mongodb+srv://SKARANJA:gD1rIw8NiVrr6bJ3@billboard.cttns.mongodb.net/Billboard?retryWrites=true&w=majority") 
db = client.Billboard
collection = db.BillboardList

@app.route('/')  
def Display_data(): 
    songs = collection.find()
    return render_template('Billboard 100.html', songs=songs) 


if __name__ == '__main__':  
        app.run(debug=True)