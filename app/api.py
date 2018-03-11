from flask import render_template, request,redirect,url_for, abort, jsonify
from app import models
from app import app, member_store, post_store


@app.route("/api/topic/all")
def all_apis():
    all_posts = post_store.get_all()
    posts = [post.__dict__() for post in all_posts]
    return jsonify(posts)


@app.route("/api/topic/show/<int:id>")
def show_api(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)
    return jsonify(post.__dict__())


@app.route("/api/topic/add", methods=['POST'])
def add_api():
    request_data = request.get_json()
    new_post = models.Post(request_data['title'], request_data['content'])
    post_store.add(new_post)
    return jsonify(new_post.__dict__())


@app.route("/api/topic/delete/<int:id>", methods=['DELETE'])
def delete_api(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)
    post_store.delete(id)
    return jsonify(post.__dict__())

@app.route("/api/topic/update/<int:id>", methods=['PUT'])
def edit_api(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)
    request_data = request.get_json()
    post.title = request_data['title']
    post.content = request_data['content']
    post_store.update(post)
    return jsonify(post.__dict__())