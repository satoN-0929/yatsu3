from flask import Flask, render_template, request, redirect, session
import sqlite3
# import os
# from pathlib import Path


app = Flask(__name__)


# @app.context_processor
# def add_staticfile():
#     def staticfile_cp(fname):
#         path = os.path.join(app.root_path, 'static', fname)
#         mtime = str(int(os.stat(path).st_mtime))
#         return '/static/' + fname + '?v=' + str(mtime)
#     return dict(staticfile=staticfile_cp)


@app.route('/index')
def index():
    # http://127.0.0.1:5000/index
    return render_template("index.html")


@app.route('/port')
def port():
    # http://127.0.0.1:5000/port
    return render_template("port.html")


@app.route('/kumamon')
def kumamon():
    # http://127.0.0.1:5000/kumamon
    return render_template("kumamon.html")


@app.route('/now')
def now():
    # http://127.0.0.1:5000/now
    return render_template("now.html")


@app.route('/pictures')
def pictures():
    # http://127.0.0.1:5000/picturs
    return render_template("pictures.html")


@app.errorhandler(404)
def notfound404(code):
    return render_template("404.html")


if __name__ == "__main__":
    # Flaskの開発用サーバーを使ってアプリを実行する
    app.run(debug=True)
