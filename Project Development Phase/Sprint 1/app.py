import mysql.connector
from flask import Flask,render_template,request,redirect,url_for,session;
import mysql.connector

import re
app=Flask(__name__)
app.secret_key = 'se'
conn=mysql.connector.connect(host='localhost',database='userinfo',user='root',password='')
cursor=conn.cursor()
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/index')
def index():
    return render_template('Index.html')
@app.route('/signin',methods=['GET','POST'])
def log():
    msg=''
    if request.method =='POST':
        email = request.form['email']
        passwword = request.form['password']
        cursor.execute('select * from customer where email=%s and password=%s',(email,passwword))
        record = cursor.fetchone()
        if record:
            session['loggedin'] = True
            session['email'] = record[1]
            return redirect(url_for('index'))
        else:
            msg = 'Incorrect username/password.Try again !'
    return render_template('login.html',msg=msg)

@app.route('/logout')

def logout():
    session.pop('loggedin',None)
    session.pop('email',None)
    return render_template('home.html')
@app.route('/signup',methods=['GET','POST'])
def register():
    msg=''
    if request.method=='POST':
        email = request.form['email']
        username=request.form['username']
        rollno=request.form['rollno']
        passwword = request.form['password']
        cursor.execute('select * from customer where email=%s and password=%s', (email, passwword))
        record = cursor.fetchone()
        if record:
            msg='Account already exist !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
            msg='Invalid email address !'
        elif not username or not passwword or not email:
            msg='Please fill out the form !'
        else:
            cursor.execute('insert into customer(email,username,rollno,password) values(%s,%s,%s,%s)',(email,username,rollno,passwword))
            conn.commit()
            cursor.close()
            msg='You have successfully Registered'
    elif request.method=='POST':
        msg='please fill out the form'
    return  render_template('signup.html',msg=msg)

@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/IT')
def IT():
    return render_template('it.html')
@app.route('/Company Questions')
def Company():
    return render_template('cq.html')
@app.route('/Opportunity')
def  Opportunity():
    return render_template('op.html')
if __name__=='__main__':
    app.run(debug=True)