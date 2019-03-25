from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(
        User, 
        related_name = 'posts',
        on_delete=models.SET_NULL,
        null=True,
    )

    creation_date= models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    upvotes = models.ManyToManyField(User, through='PostUpvote')

class Comment(models.Model):
    creation_date= models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, 
        related_name = 'comments',
        on_delete=models.SET_NULL,
        null=True,
    )
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    parent=models.ForeignKey('Comment', related_name='replies', on_delete=models.CASCADE, null=True,
                            default=None)
    content = models.TextField(null=True)
    upvotes = models.ManyToManyField(User, through='CommentUpvote')


class PostUpvote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='upvotes', on_delete=models.CASCADE)


class CommentUpvote(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comment_upvotes', on_delete=models.CASCADE)
