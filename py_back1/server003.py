from flask import Flask, request, render_template
import datetime

app = Flask(__name__)
# 태어난 년도를 입력받아 나이를 출력
# 년도를 입력 받을 화면


@app.route("/nai_view")
def nai_view():
    return render_template("nai_view.html")

# 결과를 출려하는 화면


@app.route("/nai_result")
def nai_result():
    this_year = datetime.datetime.now().year
    birth_year = int(request.args['birth_year'])
    age = this_year - birth_year
    return render_template("nai_result.html", age=age)


app.run()
