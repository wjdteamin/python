from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/human", methods=['get'])
def human():
    return render_template("/human.html")


@app.route("/human1", methods=['post'])
def human_print():
    val1 = request.form['name']
    val2 = request.form['city']
    return render_template("/human_print.html", val1=val1, val2=val2)


app.run(debug=True)


# get -> querystring -> 주소창에 값이 찍힌다.
# post -> 값이 나오지 않는다.
