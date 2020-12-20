import unittest
from app.models import Comment, User
from app import db

class CommentTest(unittest.TestCase):

        def setUp(self):
                self.user_New = User(username = 'Nadine',password = 'nadine', email = 'nadine@gmail.com')
                self.new_comment = Comment(blog_id=12345,comment='this is a blog', user = self.user_New )
        
                
        def tearDown(self):
                Comment.query.delete()
                User.query.delete()
                
                
        def test_check_instance_variables(self):
                self.assertEquals(self.new_comment.blog_id,12345)
                self.assertEquals(self.new_comment.comment,'blog love!!!')
                self.assertEquals(self.new_comment.user,self.user_James)
                
                
        def test_save_comment(self):
                self.new_comment.save_comment()
                self.assertTrue(len(Comment.query.all())>0)
                
                
        def test_get_comment_by_id(self):

                self.new_comment.save_comment()
                got_comments = Comment.get_comments(12345)
                self.assertTrue(len(got_comments) == 1)