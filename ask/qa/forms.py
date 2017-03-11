from .ino import models,User,reverse, Paginator,EmptyPage,Http404,forms,ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from .models import Question,Answer
class AskForm(ModelForm):
    class Meta:
        model=Question
        fields=['title','text']
    text=forms.CharField(widget=forms.Textarea)
    def save(self):
        answer = Question(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer
class AnswerForm(ModelForm):
    class Meta:
        model=Answer
        fields=['text','question']
    text = forms.CharField(widget=forms.Textarea)
    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer
class Signup(ModelForm):
    class Meta:
        model=User
        fields=['password','username','email']
    def create(self,request):
        user=User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password'])
        auth.login(request, user)
class Login(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass
    def clean(self):
        pass