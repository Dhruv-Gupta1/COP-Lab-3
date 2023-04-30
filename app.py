from flask import Flask, render_template,url_for,request,jsonify,session,redirect,json
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
from flask_paginate import Pagination, get_page_parameter
from datetime import datetime,timedelta
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


def time_convert(cur):
    now = datetime.now()
    time_diff= now-cur
    if(time_diff<timedelta(minutes=1)):
        return 'just now'
    elif time_diff < timedelta(hours=1):
        minutes = time_diff.seconds // 60
        return f'{minutes} minutes ago'
    elif time_diff < timedelta(days=1):
        hours = time_diff.seconds // 3600
        return f'{hours} hours ago'
    elif time_diff < timedelta(days=30):
        days = time_diff.days
        return f'{days} days ago'
    elif time_diff < timedelta(days=365):
        months = time_diff.days // 30
        return f'{months} months ago'
    else:
        time = cur.strftime("%b %d, %Y at %H:%M")
        return f'{time}'

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
            cur.execute('SELECT * FROM users WHERE UserName = % s', (username, ))
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
    cur = mysql.connection.cursor()
    cur.execute("SELECT TagName FROM tags ORDER BY QCount DESC LIMIT 5")
    tags = cur.fetchall()
    cur.execute("SELECT UserName FROM users ORDER BY Rating DESC LIMIT 10")
    top = cur.fetchall()
    cur.execute("SELECT * FROM questions ORDER BY QCreationTime DESC LIMIT 4")
    recent = cur.fetchall()
    cur.execute("SELECT * FROM questions ORDER BY QuesScore DESC")
    questions = cur.fetchall()
    cur.execute("SELECT * FROM answers ORDER BY AnsScore DESC")
    answers = cur.fetchall()
    cur.close()
    if 'loggedin' in session:
        return render_template('base_loggedin.html',questions=questions,answers = answers,recent=recent,top=top,tags=tags)
    return render_template('base.html',recent=recent,top=top,tags=tags)

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
    # if sort == 'UserName':
    #     cur.execute("SELECT * FROM users ORDER BY "+sort + " ASC LIMIT %s OFFSET %s", (per_page, offset))
    # else:
    #     cur.execute("SELECT * FROM users ORDER BY "+sort + " DESC LIMIT %s OFFSET %s", (per_page, offset))
    # users = cur.fetchall()
    if request.method == 'GET':
        page = request.args.get('page',1 , type=int)
        per_page = 5
        offset = (page - 1) * per_page
        
        cur = mysql.connection.cursor() 
        cur.execute("SELECT COUNT(*) FROM questions")
        total_count = (cur.fetchone()[0]+per_page-1)//per_page
        lower = max(page-1,1)
        higher= min(page+1,total_count)+1
        # cur.execute("SELECT * FROM questions ORDER BY "+sort + " DESC")
        if(sort=='QuesTitle'):
            cur.execute("SELECT q.*,u.* FROM questions q JOIN users u WHERE q.UserId=u.UserId ORDER BY "+sort+ " ASC LIMIT %s OFFSET %s", (per_page, offset))
        else:
            cur.execute("SELECT q.*,u.* FROM questions q JOIN users u WHERE q.UserId=u.UserId ORDER BY "+sort+ " DESC LIMIT %s OFFSET %s", (per_page, offset))
        questions = cur.fetchall()
        new_questions = []
        for question in questions:
            question_tags = json.loads(question[5])
            qid = question[0]
            cur.execute("SELECT COUNT(*) FROM answers WHERE QuesId = %s", (qid,))
            c = cur.fetchone()
            new_question = question[:5] + (question_tags,) + question[5:14] + (c[0],)
            new_questions.append(new_question)  
        cur.close()
        if 'loggedin' in session:
            pagination = Pagination(page=page, per_page=per_page, total=total_count, css_framework='bootstrap4')
            return render_template('questions.html',questions=new_questions,pagination=pagination,sort=sort,lower=lower,higher=higher)
        else:
            pagination = Pagination(page=page, per_page=per_page, total=total_count, css_framework='bootstrap4')
            return render_template('questions.html',questions=new_questions,pagination=pagination,sort=sort,lower=lower,higher=higher)

@app.route('/users/<string:sort>',methods=['GET'])
def users(sort):
    if(request.method == 'GET'):
        page = request.args.get('page',1 , type=int)
    else :
        page = 1
    per_page = 15
    offset = (page - 1) * per_page
    cur = mysql.connection.cursor() 
    cur.execute("SELECT COUNT(*) FROM users")
    total_count = (cur.fetchone()[0]+per_page-1)//per_page
    lower = max(page-1,1)
    higher= min(page+1,total_count)+1
    if sort == 'UserName':
        cur.execute("SELECT * FROM users ORDER BY "+sort + " ASC LIMIT %s OFFSET %s", (per_page, offset))
    else:
        cur.execute("SELECT * FROM users ORDER BY "+sort + " DESC LIMIT %s OFFSET %s", (per_page, offset))
    users = cur.fetchall()
    cur.close()
    pagination = Pagination(page=page, per_page=per_page, total=total_count, css_framework='bootstrap4')
    return render_template('users.html', users=users, pagination=pagination, sort=sort,lower=lower,higher=higher)

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
        question = cur.fetchone()
        question_tags = json.loads(question[5])
        new_question = question[:5] + (question_tags,) + question[6:]
        new_question1 = new_question[:3] + (time_convert(new_question[3]),) + new_question[4:]
        cur.execute("SELECT * FROM users WHERE UserId = %s",(question[6],))
        asker_details = cur.fetchone()
        cur.close()
        return render_template('quesdetail.html',question=new_question1,details=details,asker_details=asker_details)
    return render_template('quesdetail.html')



@app.route('/ask',methods=['GET','POST'])
def ask():
    if request.method == 'POST' and 'QuesTitle' in request.form and 'QuesTags' in request.form:
        if 'loggedin' in session:
            QuesTitle = request.form.get('QuesTitle')
            QuesDesc = request.form.get('QuesDesc')
            QuesTags = request.form.getlist('QuesTags')
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO questions(QuesTitle,QuesDesc,QuesTags,QuesScore,UserId,QCreationTime) VALUES (%s, %s, %s, %s, %s, %s)", (QuesTitle,QuesDesc,json.dumps(QuesTags),0,session['id'],time,))
            
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('ask'))
    return render_template('AskQuery.html')

@app.route('/answer/<int:id>',methods=['GET','POST'])
def answer(id):
    if not 'loggedin' in session:
        return redirect(url_for('login'))
    if request.method == 'POST' and 'AnsDesc' in request.form:
        if 'loggedin' in session:
            AnsDesc = request.form.get('AnsDesc')
            cur = mysql.connection.cursor()
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cur.execute("INSERT INTO answers(AnsDesc,AnsScore,QuesId,UserId,ACreationTime) VALUES (%s, %s, %s, %s, %s)", (AnsDesc,0,id,session['id'],time,))
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


        
        
@app.route('/search', methods =['GET','POST'])
def search():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from questions LIMIT 300")
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
        cur = mysql.connection.cursor()
        new_questions = []
        for question in questions:
            question_tags = json.loads(question[5])
            cur.execute("SELECT COUNT(*) FROM answers WHERE QuesId = %s", (question[0],))
            c = cur.fetchone()
            cur.execute("SELECT * FROM users WHERE UserId = %s", (question[6],))
            username = cur.fetchone()
            new_question = question[:5] + (question_tags,) + question[5:14] + (c[0],) + (username[1],)
            new_questions.append(new_question)  
        cur.close()
        return render_template('search.html', ques_list=new_questions)
    return render_template('search.html',ques_list=[])   


@app.route('/editprofile',methods=['GET','POST'])
def editprofile():
    if request.method == 'POST':
        ImageLink = request.form.get('ImageLink')
        about = request.form.get('about')
        email = request.form.get('email')
        location = request.form.get('location')
        cur = mysql.connection.cursor()
        cur.execute("UPDATE users SET UserAbout = %s, UserEmail = %s, UserLocation = %s, UserImg = %s WHERE UserId = %s",(about, email, location, ImageLink, session['id'],))
        session['image'] = ImageLink
        mysql.connection.commit()
        cur.close()
        return (redirect(url_for('myprofile')))
    return (redirect(url_for('myprofile')))


@app.route('/profile/<UserId>',methods=['GET','POST'])
def otherprofile(UserId):
    if request.method == 'GET':
        if ('loggedin' in session):
            if int(UserId)!= int(session['id']):
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM users WHERE UserId = %s",(UserId,))
                details = cur.fetchone()
                cur.close()
                return render_template('other_profile.html',details=details)
            else:
                return (redirect(url_for('myprofile')))
        else:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM users WHERE UserId = %s",(UserId,))
            details = cur.fetchone()
            cur.close()
            return render_template('other_profile.html',details=details)
    return (redirect(url_for('login')))


@app.route('/changepasswd' , methods=['GET','POST'])
def changepasswd():
    msg_pd=''
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE UserId = %s",(session['id'],))
    details = cur.fetchone()
    cur.close()
    if request.method == 'POST':
        curr_paswd = request.form.get('password')
        new_passwd = request.form.get('newpassword')
        renew_passwd = request.form.get('renewpassword')
        if new_passwd != renew_passwd:
            msg_pd = "New passwords do not match"
            return render_template('myprofile.html',msg_pd=msg_pd, details=details)
        password_hash = bcrypt.generate_password_hash(curr_paswd).decode('utf-8')
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE UserId = %s",(session['id'],))
        user_details = cur.fetchone()
        if not bcrypt.check_password_hash(user_details[3],curr_paswd):
            msg_pd = "Incorrect Password"
            return render_template('myprofile.html',msg_pd=msg_pd,details=details)
        cur = mysql.connection.cursor()
        cur.execute("UPDATE users SET UserPass = %s WHERE UserId = %s",(bcrypt.generate_password_hash(new_passwd).decode('utf-8'),session['id'],))
        cur.connection.commit()
        cur.close()
        msg_pd = "Password Changed Successfully"
        return render_template('myprofile.html',msg_pd=msg_pd,details=details)
    return (redirect(url_for('myprofile')))

@app.route('/QuesUpvote/<id>',methods=['GET','POST'])
def QuesUpvote(id):
    if ('loggedin' in session):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM questionvotes WHERE QuesId = %s AND QUserId = %s",(id,session['id'],))
        states = cur.fetchone()
        if states is None:
            cur.execute("SELECT * FROM questions WHERE QuesId = %s",(id,))
            details = cur.fetchone()
            cur.execute("UPDATE questions SET QuesScore = %s WHERE QuesId = %s",(details[4]+1,id,))
            cur.execute("INSERT INTO questionvotes (QuesId,QUserId,QState) VALUES (%s,%s,%s)",(id,session['id'],1,))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('quesdetail',id=id))
        else:
            if states[3] == 1:
                cur.execute("SELECT * FROM questions WHERE QuesId = %s",(id,))
                details = cur.fetchone()
                cur.execute("UPDATE questions SET QuesScore = %s WHERE QuesId = %s",(details[4]-1,id,))
                cur.execute("DELETE FROM questionvotes WHERE QuesId = %s AND QUserId = %s",(id,session['id'],))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('quesdetail',id=id))
            elif states[3] == 2:
                cur.execute("SELECT * FROM questions WHERE QuesId = %s",(id,))
                details = cur.fetchone()
                cur.execute("UPDATE questions SET QuesScore = %s WHERE QuesId = %s",(details[4]+2,id,))
                cur.execute("UPDATE questionvotes SET QState = %s WHERE QuesId = %s AND QUserId = %s",(1,id,session['id'],))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('quesdetail',id=id))
    return (redirect(url_for('login')))

@app.route('/QuesDownvote/<id>',methods=['GET','POST'])
def QuesDownvote(id):
    if ('loggedin' in session):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM questionvotes WHERE QuesId = %s AND QUserId = %s",(id,session['id'],))
        states = cur.fetchone()
        if states is None:
            cur.execute("SELECT * FROM questions WHERE QuesId = %s",(id,))
            details = cur.fetchone()
            cur.execute("UPDATE questions SET QuesScore = %s WHERE QuesId = %s",(details[4]-1,id,))
            cur.execute("INSERT INTO questionvotes (QuesId,QUserId,QState) VALUES (%s,%s,%s)",(id,session['id'],2,))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('quesdetail',id=id))
        else:
            if states[3] == 2:
                cur.execute("SELECT * FROM questions WHERE QuesId = %s",(id,))
                details = cur.fetchone()
                cur.execute("UPDATE questions SET QuesScore = %s WHERE QuesId = %s",(details[4]+1,id,))
                cur.execute("DELETE FROM questionvotes WHERE QuesId = %s AND QUserId = %s",(id,session['id'],))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('quesdetail',id=id))
            elif states[3] == 1:
                cur.execute("SELECT * FROM questions WHERE QuesId = %s",(id,))
                details = cur.fetchone()
                cur.execute("UPDATE questions SET QuesScore = %s WHERE QuesId = %s",(details[4]-2,id,))
                cur.execute("UPDATE questionvotes SET QState = %s WHERE QuesId = %s AND QUserId = %s",(2,id,session['id'],))
                mysql.connection.commit()
                cur.close()
                return redirect(url_for('quesdetail',id=id))
    return (redirect(url_for('login')))



@app.route('/TagSearch/<string:TagName>',methods=['GET','POST'])
def tagsearch(TagName):
    if request.method == "GET":
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM questions WHERE JSON_CONTAINS(QuesTags, '["+'"'+TagName+'"'+"]', '$')")
        details = cur.fetchall()
        new_questions=[]
        for question in details:
            question_tags = json.loads(question[5])
            cur.execute("SELECT COUNT(*) FROM answers WHERE QuesId = %s", (question[0],))
            c = cur.fetchone()
            cur.execute("SELECT * FROM users WHERE UserId = %s", (question[6],))
            username = cur.fetchone()
            new_question = question[:5] + (question_tags,) + question[5:14] + (c[0],) + (username[1],)
            new_questions.append(new_question)  
        cur.close()
        return render_template('tagsearch.html',ques_list=new_questions)
    return (redirect(url_for('home')))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8061)
