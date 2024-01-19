from flask import Flask, request, render_template, redirect

app = Flask(__name__)

todos = []
tno = 1


@app.route("/list", methods=['get'])
def list():
    return render_template("/list.html", todos=todos)


@app.route("/write", methods=['get'])
def write():
    return render_template("/write_do.html")


@app.route("/write", methods=['post'])
def write_do():
    global tno
    todo = request.form.get("title", type=str)
    tno += 1
    return redirect("/list")


app.run()
