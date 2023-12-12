from flask import Flask, render_template, request, redirect, url_for
import json
from classes import *

JSON_FILE = 'C:/Users/marsh/OneDrive/Área de Trabalho/Faculdade/P3/prompt_app/users.json'
user_list_file = open(JSON_FILE)
user_list      = json.load(user_list_file)

app = Flask(__name__)
app.config['UPLOAD_PATH'] = '/'

@app.route("/", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html") 
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in user_list['users'] and password == user_list['users'][username]['password']:
            user = user_list['users'][username]
            user = Profile(user['username'],user["first_name"],user["second_name"],user["password"],user['age'],user['posts'],user['follows'])
            return render_template("home.html", user = user)
    return render_template("login.html")

@app.route('/home', methods=['GET','POST'])
def home():
    return render_template("home.html")

if __name__ == "__main__":

    app.run(debug = True, port = 8000)