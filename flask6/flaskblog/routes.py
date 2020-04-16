#-*_coding:utf-8-*-
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'aa',
        'title' : 'blog post1',
        'content': 'first post content',
        'date_posted':'2020-04-10'

    },
     {
        'author': 'doe',
        'title' : 'blog post2',
        'content': 'second post content',
        'date_posted':'2020-04-11'
    }
]

@app.route('/')
@app.route('/home')
#route = 브라우져가 인식할 경로
def home():
    return render_template('home.html', posts=posts, title='Home')
    #posts=posts 앞에꺼는 전달할 인수 이름으로 사용하는 변수 이름. 

@app.route('/about')
#route = 브라우져가 인식할 경로
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
#route = 브라우져가 인식할 경로
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        #문자열 앞에 f를 추가하면 변수를 담아 전달 가능 파이썬3.6 이하는 format 함수 사용
        flash('Your account has been created! you are now able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET',"POST"])
#route = 브라우져가 인식할 경로
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            #get 방식으로 하면 다른 요청 파라미터를 가져오기 때문에 주의
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Please check email and password", 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
#route = 브라우져가 인식할 경로
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
#route = 브라우져가 인식할 경로
@login_required
#로그아웃 하고 강제로 여기로 들어오면 자동으로 login 으로 들어가도록 하는 함수
def account():
    return render_template('account.html', title='Account')
