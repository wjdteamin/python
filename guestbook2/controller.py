from flask import Flask, redirect, request, render_template
import model as m
import time
app = Flask(__name__)


@app.route("/list", methods=['get'])
def list():
    guestbook = m.list_information()
    return render_template("list.html", guestbook=guestbook)


@app.route("/write", methods=['post'])
def write():
    name = request.form.get("name", type=str)
    content = request.form.get("content", type=str)
    m.guestbook_save(name, content)
    return redirect("/list")


@app.route("/delete", methods=['post'])
def delete():
    gno = request.form.get("gno", type=int)
    m.guestbook_delete(gno)
    return redirect("/list")


@app.route("/update", methods=['post'])
def update():
    gno = request.form.get("gno", type=int)
    content = request.form.get("content", type=str)
    m.guestbook_update(gno, content)
    return redirect("/list")


app.run()
