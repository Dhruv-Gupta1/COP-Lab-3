from flask import Flask, render_template,url_for,request,jsonify,session,redirect,json
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
import yaml
import re
import base64
import spacy

nlp = spacy.load("en_core_web_md")

app = Flask(__name__, static_folder='static')

bcrypt = Bcrypt(app)

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
        cursor.execute('SELECT * FROM users WHERE UserName = % s', (username,))
        account = cursor.fetchone()
        if account and bcrypt.check_password_hash(account[3],password):
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
            password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
            cur.execute("INSERT INTO users(UserName,UserEmail,UserPass) VALUES (%s, %s, %s)", (username,email,password_hash))
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
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM questions ORDER BY QuesScore DESC")
        questions = cur.fetchall()
        cur.execute("SELECT * FROM answers ORDER BY AnsScore DESC")
        answers = cur.fetchall()
        cur.close()
        return render_template('base_loggedin.html',questions=questions,answers = answers)
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
            question_tags = json.loads(question[5])
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
        var2 = "SELECT q.* FROM questions q WHERE q.QuesId="
        cur.execute(var2 + str(id) + ";")
        question = cur.fetchall()
        cur.close()
        return render_template('quesdetail.html',question=question,details=details)
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


@app.route('/upvoteAns/<int:id>',methods=['GET','POST'])
def upvoteAns(id):
    if request.method == 'GET':
        if 'loggedin' in session:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM votes WHERE AnsId = %s AND UserId = %s",(id,session['id'],))
            states = cur.fetchone()
            if states is None:
                cur.execute("SELECT * FROM answers WHERE AnsId = %s",(id,))
                details = cur.fetchone()
                cur.execute("UPDATE answers SET AnsScore = %s WHERE AnsId = %s",(details[2]+1,id,))
                cur.execute("INSERT INTO votes(AnsId,UserId,State) VALUES (%s, %s, %s)", (id,session['id'],1,))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('quesdetail',id=details[5]))
            elif states[3] == 1:
                cur.execute("SELECT * FROM answers WHERE AnsId = %s",(id,))
                details = cur.fetchone()
                cur.execute("UPDATE answers SET AnsScore = %s WHERE AnsId = %s",(details[2]-1,id,))
                cur.execute("DELETE FROM votes WHERE AnsId = %s AND UserId = %s",(id,session['id'],))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('quesdetail',id=details[5])) 
            elif states[3] == 2:
                cur.execute("SELECT * FROM answers WHERE AnsId = %s",(id,))
                details = cur.fetchone()
                cur.execute("UPDATE answers SET AnsScore = %s WHERE AnsId = %s",(details[2]+2,id,))
                cur.execute("UPDATE votes SET State = %s WHERE AnsId = %s AND UserId = %s",(1,id,session['id'],))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('quesdetail',id=details[5]))
    return (redirect(url_for('login')))

@app.route('/downvoteAns/<int:id>',methods=['GET','POST'])
def downvoteAns(id):
    if request.method == 'GET':
        if 'loggedin' in session:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM votes WHERE AnsId = %s AND UserId = %s",(id,session['id'],))
            states = cur.fetchone()
            if states is None:
                cur.execute("SELECT * FROM answers WHERE AnsId = %s",(id,))
                details = cur.fetchone()
                cur.execute("UPDATE answers SET AnsScore = %s WHERE AnsId = %s",(details[2]-1,id,))
                cur.execute("INSERT INTO votes(AnsId,UserId,State) VALUES (%s, %s, %s)", (id,session['id'],2,))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('quesdetail',id=details[5]))
            elif states[3] == 2:
                cur.execute("SELECT * FROM answers WHERE AnsId = %s",(id,))
                details = cur.fetchone()
                cur.execute("UPDATE answers SET AnsScore = %s WHERE AnsId = %s",(details[2]+1,id,))
                cur.execute("DELETE FROM votes WHERE AnsId = %s AND UserId = %s",(id,session['id'],))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('quesdetail',id=details[5])) 
            elif states[3] == 1:
                cur.execute("SELECT * FROM answers WHERE AnsId = %s",(id,))
                details = cur.fetchone()
                cur.execute("UPDATE answers SET AnsScore = %s WHERE AnsId = %s",(details[2]-2,id,))
                cur.execute("UPDATE votes SET State = %s WHERE AnsId = %s AND UserId = %s",(2,id,session['id'],))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('quesdetail',id=details[5]))
    return (redirect(url_for('login')))



# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     if request.method == 'GET' and 'q' in request.form:
#         nlp = spacy.load('en_core_web_sm')
#         search =  request.args.get('q')
#         doc = nlp(search)
#         relevant_words = [token.text for token in doc if not token.is_stop and not token.is_punct]
#         cur = mysql.connection.cursor()
#         sql = "SELECT question FROM questions WHERE MATCH (question) AGAINST (%s) ORDER BY "
#         for word in relevant_words:
#             sql += "CASE WHEN question LIKE '% " + word + " %' THEN 1 WHEN question LIKE '% " + word + "' THEN 2 WHEN question LIKE '" + word + " %' THEN 3 ELSE 4 END, "
#         sql += "MATCH (question) AGAINST (%s) DESC"
#         cur.execute(sql, [search] + relevant_words + [search])
#         questions = [row[0] for row in cur.fetchall()]
#         cur.close()
#         return render_template('search.html', questions=questions)
#     return render_template('search.html',questions=[])
        
@app.route('/search', methods =['GET','POST'])
def search():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from questions")
    questons = cur.fetchall()
    cur.close()
    def get_lemmas(doc):
        return [token.lemma_ for token in doc]
    spacy.tokens.Doc.set_extension("lemmas", getter=get_lemmas, force=True)
    preprocessed_questions = [nlp(" ".join([token.lemma_.lower() for token in nlp(q[1]) if not token.is_stop])) for q in questons]
    if request.method == 'GET':
        query =  request.args.get('q')
        preprocessed_query = nlp(" ".join([token.lemma_.lower() for token in nlp(query) if not token.is_stop]))
        similarity_scores = [preprocessed_query.similarity(q) for q in preprocessed_questions]
        ranked_questions = [questons[i] for i in sorted(range(len(similarity_scores)), key=lambda k: similarity_scores[k], reverse=True)]

        questions = [q for q in ranked_questions[:5]]
        
        new_questions = []
        for question in questions:
            question_tags = json.loads(question[4])
            new_question = question[:4] + (question_tags,) + question[5:]
            new_questions.append(new_question)
        return render_template('search.html', ques_list=new_questions)
    return render_template('search.html',ques_list=[])   





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
    app.run(debug=True,port=8035)