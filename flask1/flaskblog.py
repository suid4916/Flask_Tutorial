from flask import Flask
app = Flask(__name__)
#module의 이름

@app.route('/')
@app.route('/home')
#route = 브라우져가 인식할 경로
def home():
    return "<h1>HOME PAGE!</h1>"

@app.route('/about')
#route = 브라우져가 인식할 경로
def about():
    return "<h1>About PAGE!</h1>"

#파일 직접 실행한다는 조건을 추가
if __name__ == '__main__':
    app.run(debug=True)