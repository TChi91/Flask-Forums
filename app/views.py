from flask import render_template, request,redirect,url_for, abort
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


@app.route("/topic/delete/<int:id>")
def delete_topic(id):
    try:
        post_store.delete(id)
    except ValueError:
        abort(404)
    return redirect(url_for('home'))

@app.route("/topic/show/<int:id>")
def show_topic(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)
    return render_template("show.html", post = post)

@app.route("/topic/edit/<int:id>", methods=['GET', 'POST'])
def edit_topic(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post_store.update(post)
        return redirect(url_for('home'))
    else:
        return render_template("edit.html", post = post)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404