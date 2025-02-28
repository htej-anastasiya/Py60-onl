from datetime import datetime
from flask import render_template, redirect, url_for, request
from app import app
from app.posts.posts_service import PostsService


@app.route('/posts', methods=["GET"])
def get_posts():
    posts_serv = PostsService()
    posts = posts_serv.get_posts_list()
    return render_template("posts.html", title="Travel blog", posts=posts)

@app.route('/posts/<post_id>', methods=["GET"])
def get_post(post_id):
    posts_serv = PostsService()
    post = posts_serv.get_post_by_id(post_id)
    if post is None:
        return render_template("post.html", title="Not found", post=post,  post_id=post.id)
    return render_template("post.html", title=post.title, post=post, post_id=post.id)


@app.route('/new-post',methods=["GET"])
def get_create_post_page():
    return render_template("new-post.html",title="New post" )


@app.route('/posts', methods=["POST"])
def create_post():
    title = request.form.get('title')
    content = request.form.get('content')
    posts_serv = PostsService()
    new_post = {
        'title': title,
        'content': content,
        'created_at': datetime.now()
    }
    posts_serv.create_post(new_post)
    return redirect(url_for('get_posts'))


@app.route('/update-post/<post_id>', methods=["GET"])
def get_update_post_page(post_id):
    posts_srv = PostsService()
    post = posts_srv.get_post_by_id(post_id)
    return render_template("update-post.html", title=post.title, post=post, post_id=post.id)

@app.route('/update-post/<post_id>', methods=["POST"])
def update_post(post_id):
    title = request.form.get('title')
    content = request.form.get('content')
    posts_serv = PostsService()
    updated_post = dict(new_title=title, new_content=content, updated_at=datetime.now())
    posts_serv.edit_post(post_id,updated_post)
    return redirect(url_for('get_posts'))

@app.route('/posts/<post_id>/delete', methods=["Get"])
def get_delete_post_page(post_id):
    posts_srv = PostsService()
    post = posts_srv.get_post_by_id(post_id)
    return render_template("delete-post.html", title="Delete post", post=post, post_id=post.id)

@app.route('/posts/<post_id>/delete', methods=["POST"])
def delete_post(post_id):
    posts_srv=PostsService()
    remove_post=posts_srv.delete_post(post_id)
    return redirect(url_for('get_posts'))
