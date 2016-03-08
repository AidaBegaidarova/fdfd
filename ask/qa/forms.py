from django import forms
from qa.models import Question, Answer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AskForm(forms.Form):
    title = forms.CharField(max_length=150)
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        if self._user is None or self._user.is_anonymous():
            #self._user = 1
            raise forms.ValidationError('You are not logged in.')
        return self.cleaned_data

    def save(self):
        self.cleaned_data['author_id'] = self._user.pk
        q = Question.objects.create(**self.cleaned_data)
        return q

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    #question = forms.CharField(widget=forms.HiddenInput)
    question = forms.IntegerField()

    def clean(self):
        if self._user is None or self._user.is_anonymous():
            raise forms.ValidationError('You are not logged in.')
        return self.cleaned_data

    def save(self):
        a = Answer()
        a.text = self.cleaned_data['text']
        #a.author = self._user
        a.author_id = self._user.pk
        a.question_id = self.cleaned_data['question']
        a.save()
        return a

    def clean_question(self):
        q = self.cleaned_data['question']
        if Question.objects.filter(pk=q).count() == 0:
            raise forms.ValidationError('Not enouth question')
        return q


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email',)
#
#     def save(self, commit=True):
#         user = super(UserRegisterForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         if commit:
#             user.save()
#         return user

class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def save(self):
        user = User.objects.create_user(username=self.cleaned_data['username'],
                                        email=self.cleaned_data['email'],
                                        password=self.cleaned_data['password'])
        return user

