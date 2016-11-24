from django.conf.urls import url

from . import views

app_name = 'app002'
urlpatterns = [
    url(r'^$', views.item000, name='index'),
    url(r'^t01/', views.t01, name='t01'), #item001/123 後面有東西都好
    # url(r'^t02/', views.t02, name='t02'), #item001/123 後面有東西都好
    # url(r'^t03/', views.t03, name='t03'), #item001/123 後面有東西都好
    #
    # url(r'^logout/', views.logout_view, name='logout_view'),


]
