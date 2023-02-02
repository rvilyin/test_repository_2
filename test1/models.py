from django.db import models



class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    likes = models.IntegerField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.CharField(max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.user

