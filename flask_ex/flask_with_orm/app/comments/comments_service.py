from app.base.baseservice import BaseService
from app.posts.db_model import Post
from app.comments.db_model import Comment

class CommentService(BaseService):

    def create_comment(self, comment_data: dict):
        comment = Comment(**comment_data)
        self.add_to_session(comment)
        self.commit()
        self.refresh_obj(comment)
        return comment

    
