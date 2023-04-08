from flask import Flask, render_template,url_for,request,jsonify,session,redirect,json
from flask_mysqldb import MySQL
import yaml
import re
import base64

app = Flask(__name__, static_folder='static')

app.secret_key = "Sakata-Gintoki"

db = yaml.load(open('db.yaml'),Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/login', methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE UserName = % s AND UserPass = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            session['image'] = account[4]
            return redirect(url_for('base'))
        else:
            msg = 'Incorrect username / password !'
            return render_template('login.html', msg=msg)
    return render_template('login.html', msg=msg)

@app.route('/signup', methods=['GET','POST'])
def signup():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE UserName = %s", (username,))
        cnt = cur.fetchone()
        cur.close()
        if cnt:
            msg = 'Account already exists !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !' 
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        else:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(UserName,UserEmail,UserPass) VALUES (%s, %s, %s)", (username,email,password))
            cur.execute('SELECT * FROM users WHERE UserName = % s AND UserPass = % s', (username, password, ))
            account = cur.fetchone()
            mysql.connection.commit()
            cur.close()
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            session['image'] = account[4]
            return redirect(url_for('base'))
    elif request.method == 'POST':
        msg='Please fill out the form !'
    return render_template('signup.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('image', None)
    return redirect(url_for('base'))

@app.route('/')
def base():
    if 'loggedin' in session:
        return render_template('base_loggedin.html')
    return render_template('base.html')

@app.route('/tags/<string:sort>',methods=['GET'])
def tags(sort):
    if request.method == 'GET':
        cur = mysql.connection.cursor() 
        cur.execute("SELECT * FROM tags ORDER BY "+sort)
        tags = cur.fetchall()
        cur.close()
        if 'loggedin' in session:
            return render_template('tags.html',tags=tags)
        else:
            return render_template('tags.html',tags=tags)
            
        
    return render_template('tags.html')

@app.route('/questions/<string:sort>',methods=['GET'])
def questions(sort):
    if request.method == 'GET':
        cur = mysql.connection.cursor() 
        # cur.execute("SELECT * FROM questions ORDER BY "+sort + " DESC")
        cur.execute("SELECT q.*,u.* FROM questions q JOIN users u WHERE q.UserId=u.UserId ORDER BY "+sort+ " DESC")
        questions = cur.fetchall()
        new_questions = []
        for question in questions:
            question_tags = json.loads(question[4])
            new_question = question[:4] + (question_tags,) + question[5:]
            new_questions.append(new_question)
        
        cur.close()
        if 'loggedin' in session:
            return render_template('questions.html',questions=new_questions)
        else:
            return render_template('questions.html',questions=new_questions)

@app.route('/users/<string:sort>',methods=['GET'])
def users(sort):
    if request.method == 'GET':
        cur = mysql.connection.cursor() 
        cur.execute("SELECT * FROM users ORDER BY "+sort + " DESC")
        users = cur.fetchall()
        cur.close()
        if 'loggedin' in session:
            return render_template('users.html',users=users)
        else:
            return render_template('users.html',users=users)

@app.route('/myprofile',methods=['GET','POST'])
def myprofile():
    if request.method == 'GET':
        if 'loggedin' in session:
            cur = mysql.connection.cursor() 
            cur.execute("SELECT * FROM users WHERE UserID = %s",(session['id'],))
            details = cur.fetchone()
            cur.close()
            return render_template('myprofile.html',details=details)
        else:
            return redirect(url_for('base'))

@app.route('/question/<int:id>',methods=['GET','POST'])
def quesdetail(id):
    if request.method == 'GET':
        cur = mysql.connection.cursor()
        var = "SELECT a.*,q.*,u.* FROM questions q JOIN answers a ON q.QuesId = a.QuesId  JOIN users u ON u.UserId=a.UserId WHERE q.QuesId="
        cur.execute(var + str(id) + ";")
        details = cur.fetchall()
        cur.close()
        return render_template('quesdetail.html',details=details)
    return render_template('quesdetail.html')



@app.route('/ask',methods=['GET','POST'])
def ask():
    if request.method == 'POST' and 'QuesTitle' in request.form and 'QuesDesc' in request.form and 'QuesTags' in request.form:
        if 'loggedin' in session:
            QuesTitle = request.form.get('QuesTitle')
            QuesDesc = request.form.get('QuesDesc')
            QuesTags = request.form.getlist('QuesTags')
            
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO questions(QuesTitle,QuesDesc,QuesTags,QuesScore,UserId) VALUES (%s, %s, %s, %s, %s)", (QuesTitle,QuesDesc,json.dumps(QuesTags),0,session['id'],))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('ask'))
    return render_template('AskQuery.html')

@app.route('/answer/<int:id>',methods=['GET','POST'])
def answer(id):
    if request.method == 'POST' and 'AnsDesc' in request.form:
        if 'loggedin' in session:
            AnsDesc = request.form.get('AnsDesc')
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO answers(AnsDesc,AnsScore,QuesId,UserId) VALUES (%s, %s, %s, %s)", (AnsDesc,0,id,session['id'],))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('quesdetail',id=id))
    return render_template('AddAnswer.html',id=id)
        

# @app.route('/image',methods=['POST'])
# def upload_image():
#     if request.method == 'POST':
#         image_data = request.files['image'].read()
#         cur = mysql.connection.cursor()
#         encoded_data = base64.b64encode(image_data)
#         UserId = session['id']
#         sql = "UPDATE users SET UserImg = %s WHERE UserId = %s"
#         val = (encoded_data,UserId,)
#         cur.execute(sql, val)
#         cur.connection.commit()
#         cur.close()
if __name__ == "__main__":
    app.run(debug=True,port=8034)