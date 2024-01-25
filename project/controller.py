# 1
from flask import Flask, redirect, request, render_template
import dao as d
app = Flask(__name__)

# 2
@app.route("/", methods=['get'])
def board_list():
    board = d.list()
    return render_template("/list.html", board=board)

# 3
@app.route("/write", methods=['get'])
def write_move():
    return render_template("/write.html")

# 4
@app.route("/write", methods=['post'])
def board_write():
    title = request.form.get("title", type=str)
    writer = request.form.get("writer", type=str)
    content = request.form.get("content", type=str)

    d.save(title=title, writer=writer, content=content)
    return redirect("/")

# 5
@app.route("/read", methods=['get'])
def board_read():
    bno = request.args.get("bno", type=int)
    findone = d.read(bno)
    return render_template("/read.html", findone=findone)

# 6
@app.route("/update", methods=['post'])
def board_update():
    bno = request.form.get("bno", type=int)
    title = request.form.get("title", type=str)
    content = request.form.get("content", type=str)
    d.update(bno=bno, title=title, content=content)
    return redirect("/")

# 7
@app.route("/delete", methods=['post'])
def board_delete():
    bno = request.form.get("bno", type=int)
    d.delete(bno=bno)
    return redirect("/")

# 8
app.run(debug=True)
