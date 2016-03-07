from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import resolve_url
from django.core.urlresolvers import reverse


class QuestionManager(models.Manager):

    def sort_by_date(self, order='-'):
        return self.get_queryset().order_by(order + 'added_at')

    def sort_by_rating(self, order='-'):
        return self.get_queryset().order_by(order + 'rating')

    def sort_by_id(self, order='-'):
        return self.get_queryset().order_by(order + 'id')


class AnswerManager(models.Manager):

    def sort_by_date(self, order='-'):
        return self.get_queryset().order_by(order + 'added_at')


class Question(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    rating = models.IntegerField(default=0, blank=True)
    author = models.ForeignKey(User, related_name='users_questions')
    likes = models.ManyToManyField(User, related_name='users_likes')
    objects = QuestionManager()

    def get_url(self):
        #return resolve_url('questions_id', kwargs={'id': self.pk,})
        return reverse('questions_id', kwargs={'id': self.pk})

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'questions'

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True)
    author = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    objects = AnswerManager()

    def __unicode__(self):
        return self.text

    class Meta:
        db_table = 'answers'