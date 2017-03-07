from .ino import models,User,reverse, Paginator,EmptyPage,Http404,forms,ModelForm
from .models import Question,Answer
class AskForm(ModelForm):
    class Meta:
        model=Question
        fields=['title','text']
    text=forms.CharField(widget=forms.Textarea)
    def clean(self):
        pass
class AnswerForm(ModelForm):
    class Meta:
        model=Answer
        fields=['text','question']
    text = forms.CharField(widget=forms.Textarea)
    #posi=forms.IntegerField(widget=forms.HiddenInput)
    def clean(self):
        pass
    '''def clean_posi(self):
        posi=self.cleaned_data['posi']
        try:
            t=Question.objects.get(id=posi)
        except Question.DoesNotExist:
            raise forms.ValidationError(u'Вопроса к которому вы обращаетесь не существует')
        return posi'''