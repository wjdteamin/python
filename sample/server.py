# redirect : 새로운 주소로 이동
# render_template : html을 출력


# render_template : get. html을 출력
# redirect : post. 처리하고 새로운 주소로 이동

from flask import Flask, redirect, render_template, request
app = Flask(__name__)

# 전역 변수 : 모든 함수가 접근가능한 공유 데이터
todos = []
tno = 1

# 내용을 출력하는 페이지


@app.route("/list")
def list():
    return render_template("list.html", todos=todos)


@app.route("/write", methods=['get'])
def write():
    return render_template("write.html")


@app.route("/write", methods=['post'])
def do_write():
    global tno
    title = request.form.get("title", type=str)
    todo = {"tno": tno, "title": title, "finish": False}
    print(todo)
    todos.append(todo)
    tno = tno + 1
    return redirect("/list")

# redirect -> 주소가 바뀌는 것 -> 다시 시작되는 것을 의미한다.
# 클릭하는 것은 전부 다 get이다.

@app.route("/delte")
def delete():
    tno = request.form.get('tno',type=int)
    for todo in todos:
        if todo.tno==tno:
            todos.remove(todo)
            break
    return redirect("/list")

app.run()
