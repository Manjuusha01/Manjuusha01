from flask import Flask,render_template,request
import mysql.connector

conn = mysql.connector.connect(host = 'localhost', user='root', password='Manju*2001', database='taskmanagementsystem')
mycursor = conn.cursor()

app = Flask(__name__)

user_dict={'ardra':'1234','manju':'5678'}

@app.route('/')
def page():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_home', methods=['POST'])
def login_home():
    username=request.form['username']
    pwd=request.form['password']
    if username not in user_dict:
        return render_template('login.html', msg='Invalid Username')
    elif user_dict[username]!=pwd:
        return  render_template('login.html', msg="Invald Password")
    else:
        return render_template('task.html', user=username)
    
@app.route('/view')
def view():
    query = "SELECT * FROM TASKS"
    mycursor.execute(query)
    data = mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/addnewtask',methods=['POST'])
def addnewtask():
    title = request.form.get('title')
    duedate = request.form.get('due_date')
    status = request.form.get('status')
    query = "INSERT INTO TASKS VALUES (%s,%s,%s)"
    data = (title,duedate,status)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('task.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')
@app.route('/deletetask',methods=['POST'])
def deletetask():
    tstitle = request.form.get('task_title')
    query = "DELETE FROM TASKS WHERE title LIKE '%{}%'".format(tstitle)
    mycursor.execute(query)
    data = mycursor.fetchall()
    return render_template('view.html',sqldata=data)

if __name__=='__main__':
    app.run(debug=True)
