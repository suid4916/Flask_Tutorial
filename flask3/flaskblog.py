from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
#module의 이름

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
    form = RegistrationForm()
    if form.validate_on_submit():
        #문자열 앞에 f를 추가하면 변수를 담아 전달 가능 파이썬3.6 이하는 format 함수 사용
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET',"POST"])
#route = 브라우져가 인식할 경로
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("You have been logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash("Please check email and password", 'danger')
    return render_template('login.html', title='Login', form=form)

#파일 직접 실행한다는 조건을 추가
if __name__ == '__main__':
    app.run(debug=True)