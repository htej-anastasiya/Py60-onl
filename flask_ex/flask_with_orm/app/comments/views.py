from datetime import datetime
from flask import render_template, redirect, url_for, request
from app import app
from app.comments.comments_service import CommentService
from app.posts.posts_service import PostsService


@app.route('/posts/<post_id>/add-comment', methods=["POST"])
def add_comment(post_id):
    comment_srv = CommentService()
    post_id = request.form.get('post_id')
    content = request.form.get('content')
    new_comment = {'post_id': post_id,
                   'content': content,
                   'created_at': datetime.now()
                   }
    comment = comment_srv.create_comment(new_comment)
    return redirect(url_for('get_post', post_id=comment.post_id))


@app.route('/posts/<post_id>/add-comment', methods=["GET"])
def get_add_comment_page(post_id):
    return render_template('add-comment.html', title="Add comment", post_id=post_id)
