from flask import Flask, redirect, request, render_template
import model as m

app = Flask(__name__)


@app.route("/", methods=['get'])
def list():
    guestbook = m.list_information()
    return render_template("/list.html", guestbook=guestbook)


@app.route("/write", methods=['post'])
def write():
    name = request.form.get("name", type=str)
    content = request.form.get("content", type=str)
    m.write_append(name, content)
    return redirect("/")


@app.route("/delete", methods=['post'])
def delete():
    gno = request.form.get("gno", type=int)
    m.delete_guestbook(gno)
    return redirect("/")


@app.route("/update", methods=['get'])
def update():
    gno = request.args.get("gno", type=int)
    return render_template("/update.html", gno=gno)


@app.route("/update", methods=['post'])
def update_write():
    gno = request.form.get("gno", type=int)
    content = request.form.get("content", type=str)
    m.guestbook_update(gno, content)
    return redirect("/")


app.run(debug=True)
# gb1 = dict(gno=1, name="본드", content="첫번째 내용", writeday="20204-01-22")
