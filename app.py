import flask
from flask import request, render_template, jsonify
import sqlite3 as sql
#import models as dbHandler


def create():
    con = sql.connect('data.db')
    cur = con.cursor()
    cur.execute('drop table if exists users')
    cur.execute("""create table users (
                sr integer primary key autoincrement,
                name text not null,
                age integer not null,
                mobile integer not null unique,
                email text not null unique
                );""")
    con.commit()
    con.close()

def insert(name, age, mobile, email):
    con = sql.connect('data.db')
    cur = con.cursor()
    cur.execute("INSERT INTO users (name,age,mobile,email) VALUES (?,?,?,?)", (name,age,mobile,email))
    con.commit()
    con.close()
    
def getUsers():
    con = sql.connect("data.db")
    cur = con.cursor()
    cur.execute("SELECT name, age, mobile, email FROM users")
    users = cur.fetchall()
    con.close()
    return users
        
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods =['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST','GET'])
def home():
    create()
    if request.method=='POST':
        name = request.form['name']
        age = request.form['age']
        mobile = request.form['mobile']
        email = request.form['email']
        dbHandler.insert(name, age, mobile, email)
        users = dbHandler.getUsers()
        return render_template('add.html', users=users)
    else:
        return render_template('index.html')

    

if __name__ == '__main__':
    app.run(debug=True)
