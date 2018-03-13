from flask import request, abort, jsonify, render_template
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
    try:
        result = jsonify(post.__dict__())
    except AttributeError:
        result = abort(404, f"Topic with id: {id} doesn't exist")
    return result


@app.route("/api/topic/add", methods=['POST'])
def add_api():
    request_data = request.get_json()
    try:
        new_post = models.Post(request_data['title'], request_data['content'])
        post_store.add(new_post)
        result = jsonify(new_post.__dict__())
    except KeyError:
        result = abort(400, f"Couldn't parse the request data !")
    return result


@app.route("/api/topic/delete/<int:id>", methods=['DELETE'])
def delete_api(id):
    post = post_store.get_by_id(id)
    try:
        post_store.delete(id)
        result = jsonify(post.__dict__())
    except ValueError:
        result = abort(404, f"Topic with id: {id} doesn't exist")
    return result


@app.route("/api/topic/update/<int:id>", methods=['PUT'])
def edit_api(id):
    post = post_store.get_by_id(id)
    request_data = request.get_json()
    try:
        post.title = request_data['title']
        post.content = request_data['content']
        post_store.update(post)
        result = jsonify(post.__dict__())
    except AttributeError:
        result = abort(404, f"Topic with id: {id} doesn't exist")
    except KeyError:
        result = abort(400, f"Couldn't parse the request data !")
    return result


@app.errorhandler(400)
def bad_request(error):
    return jsonify(message = error.description)