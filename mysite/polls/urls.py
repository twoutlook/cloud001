#polls/urls.py

from django.conf.urls import url

from . import views

app_name = 'polls'
# urlpatterns = [
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#     # ex: /polls/5/
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

#     # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^sop$', views.sop, name='sop'),
    url(r'^sop/(?P<sop_id>[0-9]+)/$', views.sop_detail, name='sop_detail'),



    url(r'^$', views.index, name='index'),

   # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),




    url(r'^feedback/$', views.feedback, name='feedback'),
#     # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#

    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
