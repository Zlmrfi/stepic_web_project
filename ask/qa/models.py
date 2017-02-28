from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,EmptyPage
from django.http import Http404
def paginate(request,qs):
    try:
        limit=int(request.GET.get('limit',10))
    except:
        limit=10
    if limit>100:
        limit=10
    try:
        page=int(request.GET.get('page',1))
    except:
        raise Http404
    paginator=Paginator(qs,limit)
    try:
        page=paginator.page(page)
    except EmptyPage:
        page=paginator.page(paginator.num_pages)
    return page
class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
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
    def __unicode__(self):
        return self.title
    def get_url(self):
        return '/question/{}'.format(self.id)
class Answer(models.Model):
    text=models.TextField(blank=True)
    added_at=models.DateTimeField(auto_now_add=True)
    question=models.ForeignKey(Question,null=True,on_delete=models.SET_NULL)
    author = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title