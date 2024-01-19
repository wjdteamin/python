# 사용자의 요청에 응답하는 서버개발 : 백엔드 + 화면
# 리눅스에서는 기능 따로 화면따로 깔아야 한다. <=> 윈도우는 계산기 깔면 화면 + 기능 다 깔려진다.

# 프레임워크 - 필요한 기능들을 부품화해서 조립하는 방식

# templates - html, static - css, js


from flask import Flask, render_template, request

# 서버 프로그램을 만드는 것이다.
app = Flask(__name__)
# (__name__)은 현재 타입이다. 이거는 외워야한다.

# 기능

# 외부적으로 보이는 이름 -> 배포서술자(deployment descriptor : 함수와 주소의 쌍 )

"""
@app.route("/help")
# help는 서버가 없으면 의미가 없다.
# 내부적으로 보이는 이름 -> aaa
def aaa():
    # 플라스크 함수의 리턴은 반드시 문자열
    return render_template("name.html")


# 현재 서버의 모든 url을 출력해라.
print(app.url_map)


@app.route("/apple")
def apple():
    # 함수에 인자를 보내는 게 아니라. 찾는 것이다.
    val = request.args["name"]
    return render_template("index.html", val=val)

    내가 한번 해봤던 것 -> 실행은 된다. 개판이기는 하지만
"""

# 실행되는 url : 127.0.0.1:5000
# debug란 개발 모드
#  debug=True 자동 저장(업데이트) 그런 느낌
# debug=True를 사용하려면 터미널에 python server.py를 추가로 작성해야 사용이 된다.


# 어떤 작업을 하려면 화면을 보여준다.(get) + 결과를 출력한다.(post)
# 이름을 입력받아 출력
@app.route("/name", methods=['get'])
def name_input():
    return render_template("name.html")


@app.route("/name", methods=['get'])
def name_print():

    name = request.form["name"]
    # get방식 요청 데이터 : request.args -> 보여준다.
    # post방식 요청 데이터 : request.form -> 처리하고 보여준다.
    # 사용자의 요청을 가져오는 것을 request라고한다.
    return render_template("name_result.html", name=name)
    # name=name은 인자의 이름을 주기 위해서 하는 것이다.

# 값 여러개 받는 것도 가능하다. 방식은 똑같다. return할 때 여러개 보낼 수 있다는 의미다.


app.run(debug=True)
