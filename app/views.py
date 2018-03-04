from flask import render_template, request,redirect,url_for
from app import models
from app import app, member_store, post_store

@app.route("/")
@app.route("/index")
def home():
    posts = post_store.get_all()
    return render_template("index.html", posts = posts)


@app.route("/topic/add", methods=['GET', 'POST'])
def add_topic():
    if request.method == 'POST':
        new_post = models.Post(request.form['title'] , request.form['content'])
        post_store.add(new_post)
        return redirect(url_for('home'))
    else:
        return render_template("add_topic.html")
