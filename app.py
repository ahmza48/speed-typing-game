from flask import Flask, render_template,session,request
from player import Player
from flask_session import Session
from DBHandler import DBHandler
from datetime import date
import pymysql
import random
import time

app = Flask(__name__,template_folder='template')

app.secret_key ="secretkey"
app.config['SESSION_TYPE']='filesystem'
app.config["SESSION_PERMANENT"]=False
Session(app)


@app.route('/')
def loginPage():
    print('rendering login page')
    return render_template('login.html')

@app.route('/loggedin',methods=['POST'])
def login():
    print('after login form')
    email = request.form["email"]
    password = request.form["password"]
    print(password)
    print(email)
    db = DBHandler('localhost', 'root', 'password', 'STG', 3307)
    isVerified = db.verify_player(email,password)
    if isVerified:
        session["id"] = isVerified[0][0]
        print(session["id"])
        session["username"] = isVerified[0][1]
        session["email"] = isVerified[0][2]
        session["password"] = isVerified[0][3]
        session["maxscore"] = isVerified[0][4]
        return render_template('welcome.html',name=session["username"])
    else:
        return render_template('login.html',msg='Login Failed! Try Again')


@app.route('/register')
def register():
    return render_template('registeration.html')


@app.route('/registered', methods=["POST"])
def registered():
    print('after regiseration form')
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    maxscore=0
    print(name,email,password)
    player = Player(name,email,password,maxscore)
    #print(name, age, city, profession)
    db = DBHandler('localhost', 'root', 'password', 'STG', 3307)
    isRegister = db.register_player(player)
    if isRegister:
        return render_template("/login.html")
    else:
        return render_template("registeration.html", msg="Registration Failed! Try Again. User with this email already exists")


@app.route('/game')
def game():
    # randomNumber=random.randint(0, 69)
    # word=random_words[randomNumber]
    name=session.get("username")
    maxscore=session.get("maxscore")
    isVerify=session.get("username")
    if isVerify!=None:
        return render_template('/game.html',name=name,maxscore=maxscore)
    else:
        return render_template('login.html',msg='Login First!')

# Updating Score of user in database
@app.route('/update-score',methods=['POST'])
def updateScore():
    score = request.json.get('score')
    name = session.get("username")
    email = session.get("email")
    password = session.get("password")

    try:
        db = DBHandler('localhost', 'root', 'password', 'STG', 3307)
        print('Object created')
        isUpdated = db.update_score(score, email, password)
        if isUpdated:
            return 'Score Updated Successfully'
        else:
            return 'Couldn\'t Update Score'
    except Exception as e:
        print('Error:', str(e))
        return 'An error occurred during score update'



@app.route('/logout')
def logout():
    session.clear()

    # SESSION CAN BE CLEARED THIS WAY AS WELL!

    session["id"]=None
    session["username"]=None
    session["email"]=None
    session["password"]=None
    session["max_score"]=None

    return render_template('login.html')


if __name__ == '__main__':
    app.run(port=4002)
