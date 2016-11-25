from django.conf.urls import url, include

from . import views

app_name = 'flowchart'
urlpatterns = [
    url(r'^part/$', views.view_flowchart_list, name='view_flowchart_list'),
    url(r'^part/(?P<item_id>[_A-Za-z0-9-\#\\+]+)', views.view_flowchart, name='view_flowchart'), #item001/123 後面有東西都好

    # url(r'^/$', views.view_flowchart_list, name='view_flowchart_list'),
    # url(r'^/(?P<item_id>[_A-Za-z0-9-\#\\+]+)', views.view_flowchart, name='view_flowchart'), #item001/123 後面有東西都好

]
