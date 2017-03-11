from .models import Question,Answer,paginate
from django.http import HttpResponseNotFound,HttpResponse,HttpResponseRedirect
from django.views.decorators.http import require_GET
import os
from .forms import  AskForm,AnswerForm,Signup,Login
from django.shortcuts import render
from django.contrib import auth
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def test(request, *args, **kwargs):
    return HttpResponse('OK')
def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = Login()
    return render(request, os.path.join(BASE_DIR, 'qa/templates/post.html'), {
        'form': form
    })
def sign(request, *args,**kwargs):
    if request.method=='POST':
        form=Signup(request.POST)
        if form.is_valid():
            u=form.create()
            return HttpResponseRedirect('/')
    else:
        form=Signup()
    return render(request,os.path.join(BASE_DIR,'qa/templates/post.html'), {
        'form':form
    })
def ask(request, *args, **kwargs):
    if request.method=='POST':
        form=AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            ask=form.save()
            url=ask.get_url()
            return HttpResponseRedirect(url)
    else:
        form=AskForm()
    return render(request,os.path.join(BASE_DIR,'qa/templates/post.html'),{
        'form':form,
    })
@require_GET
def httppopr(request,*args,**kwargs):
    return httppage(request,Question.objects.popular())
@require_GET
def httppage(request,*args,**kwargs):
    if request.GET.get('page') is None:
        return HttpResponse('OK')
    if not args:
        w = Question.objects.new()
    else:
        w=args[0]
    page=paginate(request,w)
    page.baseurl='/?page='
    return render(request,os.path.join(BASE_DIR,'qa/templates/pag.html'),
                  {
                      'page': page,
                  }
                                               )
def qust(request,ido,*args,**kwargs):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form._user= request.user
        if form.is_valid():
            ans = form.save()
            url = ans.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()
    try:
        q=Question.objects.get(id=ido)
        a=Answer.objects.filter(question__id=ido) or None
    except Question.DoesNotExist:
        return HttpResponseNotFound()
    return render(request,os.path.join(BASE_DIR,'qa/templates/quest.html'),
                  {   'q': q,
                      'a':a,
                      'form':form,
                  })