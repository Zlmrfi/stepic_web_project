from django.db import models
from django.contrib.auth.models import User
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')[0]
    def popular(self):
        return self.order_by('-rating')
class Question(models.Model):
    title=models.CharField(max_length=255,blank=True)
    text=models.TextField(blank=True)
    added_at=models.DateTimeField(auto_now_add=True)
    rating=models.IntegerField(blank=True,null=True)
    author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    likes=models.ManyToManyField(User,related_name='likes_set',blank=True)
    objects=QuestionManager()
    def __str__(self):
        return self.title
class Answer(models.Model):
    text=models.TextField(blank=True)
    added_at=models.DateTimeField(auto_now_add=True)
    question=models.ForeignKey(Question,null=True,on_delete=models.SET_NULL)
    author = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)