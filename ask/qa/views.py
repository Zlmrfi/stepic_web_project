from .models import Question,Answer,paginate
from django.http import HttpResponseNotFound,HttpResponse,HttpResponseRedirect
from django.views.decorators.http import require_GET
import os
from .forms import  AskForm,AnswerForm
from django.shortcuts import render
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def test(request, *args, **kwargs):
    return HttpResponse('OK')
def ask(request, *args, **kwargs):
    if request.method=='POST':
        form=AskForm(request.POST)
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
    #print(len(args))
    if not args:
        w = Question.objects.new()
    else:
        w=args[0]
    #print(request.GET.get('page'))
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