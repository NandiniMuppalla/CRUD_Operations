from flask import Flask,render_template,request
import sqlite3
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')
@app.route('/register')
def register():
    return render_template("register.html")
@app.route('/insert',methods=["post","get"])
def insert():
    conn=sqlite3.connect('flask_crud.db')
    cur=conn.cursor()
    u=request.form['username']
    p=request.form['pwd']
    e=request.form['email']
    g=request.form['gender']
    cur.execute("insert into register values(?,?,?,?)",(u,p,e,g))
    conn.commit()
    return "data inserted successfully"
@app.route('/login')
def login():
   return render_template("login.html")
@app.route('/validate',methods=["post","get"])
def validate():
    u=request.form['uname']
    p=request.form['pwd']
    conn=sqlite3.connect('flask_crud.db')
    cur=conn.cursor()
    query="select * from register where username=='"+u+"' and password=='"+p+"' "
    cur.execute(query)
    x=cur.fetchone()
    if x[0]==u and x[1]==p:
        cur.execute("select * from register where username=='"+u+"'")
        data=cur.fetchone()
        return render_template('select.html',details=data)
    
    else:
        return "invalid login"
@app.route('/update',methods=['post'])
def update():
    u=request.form['uname']
    p=request.form['pwd']
    e=request.form['email']
    g=request.form['gen']
    conn=sqlite3.connect('flask_crud.db')
    cur=conn.cursor()
    query="update register set password='"+p+"',email='"+e+"',gender='"+g+"'"
    cur.execute(query)
    data=cur.fetchone()
    conn.commit()
    return "update successfully"
app.run(debug=True,port=8888)
