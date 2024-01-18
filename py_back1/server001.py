from flask import Flask, request
# class -> 사용자 정의 자료혀을 만드는 방법. 파이썬의 모든 타입은 클래스

# __name__은 현재 파일의 이름 ->  Flask 웹서버 객체를 생성
# 서버는 사용자 요청을 기다리다가 요청이 들어오면 처리해주는 프로그램이다.
# Flask 웹서버는 5000번 포트로 사용자 요청을 대기한다.
app = Flask(__name__)
# 함수에 주소가 들어있다.

# 사용자가 만든 flask는 앞이 대문자다.

# annotation : 낙인역할이다. 사용자가 hello라고 요청하면 된다..


# hello라는 함수는 낙인이 찍혀있다. 그래서 사용자가 hello라고 요청을 보내면 서버가 동작을 한다.
# /hello라는 낙인을 찍혀있는 거여서 함수와 app.route("이름")의 이름이 같을 필요는 없다.
@app.route("/hello")  # 낙인이라고 생각하면 된다
def hello1():
    return "hello flask"


@app.route("/hello2")  # 낙인이라고 생각하면 된다
def insa():
    return "안녕하세요"


@app.route("/hello3")
def add():
    # print(request)
    # 사용자가 요청한 정보를 담는 변수 ->request

    # print(request.args)
    val = request.args['val']

    return val
#  내가 주소를 http://localhost:5000/hello?val=10이라 주면 함수에서는 val값이 10을 받는다.
#   val = request.args['val'] -> request.args는 값을 볼 수 있게 해주는 거 같다.
#   그리고 원하는 키?를 넣으면 val안에 내가 입력했던 값이 저장되는 거 같다.
#   그걸 리턴하면 값을 페이지에 보일 수 있게 해준다.

    # request로 전달받은 값은 무조건 글자


@app.route("/hello4")
def 제곱():
    val = int(request.args['val'])
    result = val * val
    return f'제곱 결과는 {result}입니다.'


@app.route("/hello5")
def 체중():
    val = int(request.args['val'])  # 입력한 값이 val에 저장된다.
    num = val - 105
    return f'적정체중은 {num}입니다.'


app.run()

# 사용자 http://localhost:5000/hello?val=10

# request.args['val']로 val의 값을 꺼낼 수 있다.
# 파이썬 {'val':'10'}


# form의 사용자가 server.py에 있는 def 제곱을 실행시키는 방법이 @approute()로 찾아주는 역할이다.???
