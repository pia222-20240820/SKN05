from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>반갑습니다. 메인페이지 입니다.</h1>"

@app.route("/list1")
def home2():
  return "<h1>리스트 정보는.... 다음과 같습니다</h1>"

@app.route("/list2")
def home3():
  return "<h1>사용자 정보는 다음과 같습니다.</h1>"

if __name__ == "__main__":
  app.run()