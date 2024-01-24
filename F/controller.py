from flask import Flask, redirect, render_template, request
import dao as d

app = Flask(__name__)


@app.route("/", methods=['get'])
def list():
    value = d.findall()
    return render_template("/list.html", list=value)


@app.route("/read", methods=['get'])
def read():
    bno = request.args.get("bno", type=int)
    value = d.findone(bno)
    return render_template("/read.html", read=value)


@app.route("/write", methods=['get'])
def write():
    return render_template("/write.html")


@app.route("/write", methods=['post'])
def save():
    title = request.form.get("title", type=str)
    nickname = request.form.get("nickname", type=str)
    content = request.form.get("content", type=str)
    d.save(title=title, nickname=nickname, content=content)
    return redirect("/")


@app.route("/delete", methods=['post'])
def delete():
    bno = request.form.get("bno", type=int)
    d.delete(bno)
    return redirect("/")


@app.route("/update", methods=['get'])
def correction():
    bno = request.args.get("bno", type=int)
    return render_template("/update.html", bno=bno)


@app.route("/update", methods=['post'])
def update():
    bno = request.form.get("bno", type=int)
    title = request.form.get("title", type=str)
    content = request.form.get("content", type=str)
    d.update(bno=bno, title=title, content=content)
    return redirect("/")


# erd 설계 -> ???

# 데이터 : model
# 모델을 다루는 클래스 : DAO -> Data Access Object라고 한다. (DAO, 다오)

# 상품 dao
# 검색 : 전체출력, 상품하나의 상세 정보, 기능 별 검색, 인기 순 검색(top 검색), 가격 높은 순, 낮은 순 검색, 구매 많은 순, 적은 순
# 분야 별 검색, 세일에 관한 검색,  내가 자주 구매했던 상품, 구매할만한 상품 -> 전부 다 read에 관한 것이다 .

# 코딩을 하는 사람보다는 기획하는 사람이 더욱 더 중요하다.

# 추가(save), 전체출력(findall), 하나출력(findone), 변경(update), 삭제(delete)

# 글 : 글번호, 제목, 내용, 닉네임, 조회수

app.run(debug=True)

# 컨트롤러 구성
# 1. 주소 지정(필수)
# 2. request에서 값을 가져온다.
# 3. dao를 부른다.
# 4. html 또는 redirect를 사용한다.
