# 이름과 나이를 입력받아 다음과 같이 출력한다.
# 홍길동님은 성년입니다. or 홍길동님은 미성년입니다.
# 단 성년인 경우 글자색은 파랑, 미성년인 경우 글자색은 빨강

from flask import Flask, render_template, request
app = Flask(__name__)

# @만들때 주소는 항상 /다.


@app.route("/work1", methods=['get'])
def work_input():
    return render_template("/work_input1.html")


@app.route("/work1", methods=['post'])
def work_print():
    irum = request.form.get('irum', type=str)
    #     irum =request.form.get('irum', type=str, default='홍길동') 타입을 정하고, 기본값을 정할 때 사용한다.
    nai = request.form.get('nai', type=int)
    # if나 for는 flask 또는 html에서 가능하다.

    is_adult = nai >= 18
    return render_template("/work_result1.html", irum=irum, nai=nai, is_adult=is_adult)
    # 값을 3개 보낸다.

# 메소드를 생략하면 get이라는 의미를 가지고 있기 때문에(@ 주소가 같은 경우)


app.run(debug=True)
