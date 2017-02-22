from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    text = models.CharField(max_length=1000,default="")
    title = models.CharField(max_length=100, default="")
    image = models.FileField(default="",upload_to='blog_images/')
    create_time = models.DateTimeField(auto_now_add=True)
    upload_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) :
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=30,default="")
    text = models.CharField(max_length=300,default="")
    create_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + " : " + self.title
