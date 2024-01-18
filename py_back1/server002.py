from flask import Flask, request, render_template


app = Flask(__name__)

# 사용자가 입력한 값을 html로 출력


@app.route("/sample1")
def sample1():
    val = request.args['val']
    return render_template("sample.html", result=val)
# 인자를 넘길때, val이라는 값을 result에 넣어서 보낸다.
# html로 보내려면 render_template을 이용한다.


# 덧셈을 입력할 화면을 출력한다.
@app.route("/add_view")
def sample2_view():
    return render_template("sample2_view.html")

# /add?val1=10&val2=24


@app.route("/add")
def sample2():
    val1 = int(request.args['val1'])
    val2 = int(request.args['val2'])
    result = val1 + val2
    return render_template("sample1.html", result=result)



app.run()
