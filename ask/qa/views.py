from .models import Question,Answer,paginate
from django.http import HttpResponseNotFound,HttpResponseBadRequest, HttpResponse
from django.views.decorators.http import require_GET
import os
from django.shortcuts import render
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def test(request, *args, **kwargs):
    return HttpResponse('OK')
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
@require_GET
def qust(request,ido,*args,**kwargs):
    try:
        q=Question.objects.get(id=ido)
        a=Answer.objects.filter(question__id=ido)
    except Question.DoesNotExist or Answer.DoesNotExist:
        return HttpResponseNotFound()
    return render(request,os.path.join(BASE_DIR,'qa/templates/quest.html'),
                  {   'q': q,
                      'a':a,
                  })