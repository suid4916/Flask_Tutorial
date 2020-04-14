from flask import Flask, render_template, url_for
app = Flask(__name__)
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

#파일 직접 실행한다는 조건을 추가
if __name__ == '__main__':
    app.run(debug=True)