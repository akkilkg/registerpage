import flask
from flask import render_template ,request
from flask import Flask
import pymongo
app = Flask(__name__)
con = pymongo.MongoClient()
db = con['web']
collections = db['details']
@app.route('/')
def home():
    return render_template('h.html')
@app.route('/welcome', methods=["GET","POST"])
def welcome():
    firstname = request.form.get('fname')
    lastname = request.form.get('lname')
    mail = request.form.get('mail')
    fullname = firstname + " " + lastname
    collections.insert_one({'fname':firstname,'lname':lastname,'fullname':fullname,'mail':mail})
    return render_template('welcome.html',name = fullname)
app.run(debug=True,port=7000)

