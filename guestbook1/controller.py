from flask import Flask, redirect, render_template, request
# import flask as f라고 해도 된다.
import model as m

# 플라스크 앱(백엔드 서버)을 생성. 인자는 현재 파일의 이름
app = Flask(__name__)


# 방명록을 출력 : 127.0.0.1: 5000
# @app.route 가지고 찾아서 함수를 실행 시키는 것이다.
@app.route("/list", methods=['get'])
def list():
    # 모델에서 데이터를 달라고 요청해야한다. 그게 정확하게 맞는지 확인을 하기위해서
    # 모델에서 함수를 사용하는 이유는 분리하기 위해서 사용하는 것이다.
    # controller에서 moder에 직접적으로 접급하지 못하게 해야한다.
    guestbook = m.findall()

    # list.html에 guestbook에 넘길 것이다. 그래서 return할 때 같이 보내는 것이다.
    # 근데 이름이 없어서 guestbook이라는 이름을 붙여서 사용한다.
    return render_template("list.html", guestbook=guestbook)


@app.route("/write", methods=['post'])
def write():
    content = request.form.get('content', type=str)
    m.content_append(content=content)
    return redirect('/list')


@app.route("/delete", methods=['post'])
def delete():
    gno = request.form.get("gno", type=int)
    m.delete(gno)
    return redirect("/list")


# 서버를 개발자 모드(변경하면 자동 재실행)로 실행
app.run(debug=True)

# 컨트롤로는 주소 공급, 모델과 뷰를 연결해주는 역할을 해준다. list.html- > 뷰, m.guestbook -> 모델


# get -> 눌러서 넘어가는 것이라 생각해라.
