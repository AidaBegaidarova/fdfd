from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#from django.http.Http404 import HttpResponseNotFound
from django.http import HttpResponse
from django.contrib.auth.views import login, logout

def ret404():
    return HttpResponse(status=404)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/$', include(admin.site.urls)),
    url(r'^$', 'qa.views.new_questions', name='new_questions'),
    url(r'^signup/$', 'qa.views.signup'),
    url(r'^question/(?P<id>[a-zA-Z0-9]*)/$', 'qa.views.question', name='questions_id'),
    url(r'^ask/$', 'qa.views.add_question', name='add_question'),
    #url(r'^popular/([/a-zA-Z0-9]*)$', 'qa.views.popular_questions', name='popular_questions'),
    url(r'^popular/$', 'qa.views.popular_questions', name='popular_questions'),
    url(r'new/([/a-zA-Z0-9]*)$', 'qa.views.test'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^answer/$', 'qa.views.add_answer', name='add_answer'),
)
