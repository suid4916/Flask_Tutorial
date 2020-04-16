#-*-coding:utf-8-*-
from flaskblog import app

#파일 직접 실행한다는 조건을 추가
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)