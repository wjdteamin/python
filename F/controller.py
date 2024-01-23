from flask import Flask, redirect, render_template, request
import dao as d

app = Flask(__name__)


@app.route("/", methods=['get'])
def list():
    value = d.findall()
    return render_template("list.html", list=value)


@app.route("/read", methods=['get'])
def read():
    bno = request.args.get("bno", type=int)
    value = d.findone(bno)
    return render_template("read.html", read=value)


@app.route("/write", methods=['get'])
def write():
    return render_template("write.html")


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


app.run(debug=True)
