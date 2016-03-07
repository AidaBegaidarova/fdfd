from django import forms
from qa.models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=150)
    text = forms.CharField(widget=forms.Textarea)

    def save(self):
        self.cleaned_data['author_id'] = 1
        q = Question.objects.create(**self.cleaned_data)
        return q

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    #question = forms.CharField(widget=forms.HiddenInput)
    question = forms.IntegerField()

    def save(self):
        a = Answer()
        a.text = self.cleaned_data['text']
        a.author_id = 1
        a.question_id = self.cleaned_data['question']
        a.save()
        return a

    def clean_question(self):
        q = self.cleaned_data['question']
        if Question.objects.filter(pk=q).count() == 0:
            raise forms.ValidationError('Not enouth question')
        return q