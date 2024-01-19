# 12 ~ 2 겨울 회색, 3 ~ 5 봄 초록, 6 ~ 8 여름 파랑, 9 ~ 11 가을 보라
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/month", methods=['get'])
def month_input():
    return render_template("start.html")


@app.route("/month", methods=['post'])
def month_print():
    month = request.form.get("month", type=int)
    season = '겨울'
    style = 'gray'
    # 타입을 꼭 지정해줘야한다.

    # html에서 하기 싫으면 여기서 처리해서 가져가도 된다
    if 3 <= month <= 5:
        season = '봄'
        style = 'green'
    elif 6 <= month <= 8:
        season = '여름'
        style = 'blue'
    elif 9 <= month <= 11:
        season = '가을'
        style = 'purple'
    # 처음부터 만들어서 보내도 된다.

    # mvc -> back이 front까지
    # rest -> back, front 별개

    return render_template("month_print.html", season=season, style=style)


app.run(debug=True)
