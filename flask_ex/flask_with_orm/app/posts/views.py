from flask import render_template
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
        return render_template("post.html", title="Not found", post=post)
    return render_template("post.html", title=post.title, post=post)


