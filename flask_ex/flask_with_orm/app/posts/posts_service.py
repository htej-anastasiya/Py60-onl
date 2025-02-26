from app.base.baseservice import BaseService
from app.posts.db_model import Post


class PostsService(BaseService):
    def get_posts_list(self):
        posts = self.query(Post).order_by(Post.id).all()
        return posts

    def create_post(self, post_data: dict):
        new_post = Post(**post_data)
        self.add_to_session(new_post)
        self.commit()
        self.refresh_obj(new_post)
        return new_post

    def get_post_by_id(self, post_id):
        post = self.query(Post).filter(Post.id==post_id).first()
        if not post:
            return None
        return post

    def edit_post(self, post_id, updated_post:dict):
        post = self.query(Post).filter(Post.id == post_id).first()
        post.title = updated_post["new_title"]
        post.content =updated_post["new_content"]
        post.updated_at=updated_post["updated_at"]
        self.add_to_session(post)
        self.commit()
        self.refresh_obj(post)
        return post


