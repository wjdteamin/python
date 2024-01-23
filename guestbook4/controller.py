from flask import Flask, request, redirect, render_template
import dao
app = Flask(__name__)


# 방명록 출력
@app.route("/")
def list():
    result = dao.findall()
    return render_template("list.html", result=result)


# 방명록 추가
# 방명록 사이트 이동 -> 글 작성

# post는 작업을 처리 -. 처리가 끝났으면 다른 작업하러 이동한다.
@app.route("/write", methods=['post'])
def write():
    nickname = request.form.get('nickname', type=str)
    content = request.form.get('content', type=str)
    dao.save(nickname=nickname, content=content)
    return redirect("/")


# 방명록 삭제


@app.route("/delete", methods=['post'])
def delete():
    gno = request.form.get("gno", type=int)
    dao.delete(gno)
    # 넘기는 인자가 하나면 굳이 이름을 지정하지 않아도 된다.
    return redirect("/")

# 값을 꺼내고, 함수 호출, return을 한다. 처음과 끝은 거의 고정이라고 생각하면 편하다.


app.run(debug=True)
