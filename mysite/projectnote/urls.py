# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import HomePageView, FormHorizontalView, FormInlineView, PaginationView, FormWithFilesView, \
    DefaultFormView, MiscView, DefaultFormsetView, DefaultFormByFieldView

# by Mark
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home$', HomePageView.as_view(), name='home'),
    url(r'^test1$', views.test1, name='test1'),
    url(r'^test2$', views.test2, name='test2'),
    url(r'^p1$', views.test1, name='p1'),
    # url(r'^flowchart$', views.flowchart, name='flowchart'),
    # url(r'^flowchart_list$', views.flowchart_list, name='flowchart_list'),
    url(r'^flowchart$', views.flowchart_list, name='flowchart_list'),
    url(r'^flowchart/(?P<item_id>[_A-Za-z0-9-\#\\+]+)', views.flowchart, name='flowchart'), #item001/123 後面有東西都好

    url(r'^employeev2$', views.employeev2, name='employeev2'),
    url(r'^trans$', views.trans, name='trans'),
    # url(r'^employee$', views.employee, name='employee'),
    url(r'^smm', views.smm, name='smm'),
    url(r'^step0', views.step0, name='step0'),
    url(r'^step1', views.step1, name='step1'),
    url(r'^bymonth', views.bymonth, name='bymonth'),
    url(r'^step2', views.step2, name='step2'),
    url(r'^step3a', views.step3a, name='step3a'),

    # 2016-12-05 可以設定截止日期
    url(r'^step3ext/(?P<item_id>[_A-Za-z0-9-\#\\+]+)', views.step3ext, name='step3ext'),

    url(r'^step3$', views.step3, name='step3'),
    # url(r'^step3a', views.step3a, name='step3a'),



    # url(r'^fc/$', views.view_flowchart_list, name='view_flowchart_list'),
    # url(r'^fc2/$', views.Flowchartprocess2, name='Flowchartprocess2'),
    # url(r'^fc3/$', views.Flowchartprocess3, name='Flowchartprocess3'),
    # url(r'^p1/$', views.p1, name='p1'),
    # url(r'^fc/(?P<item_id>[_A-Za-z0-9-\#\\+]+)', views.view_flowchart, name='view_flowchart'), #item001/123 後面有東西都好




    # url(r'^test1$', DefaultFormsetView.as_view(), name='formset_default'),
    url(r'^formset$', DefaultFormsetView.as_view(), name='formset_default'),
    url(r'^form$', DefaultFormView.as_view(), name='form_default'),
    url(r'^form_by_field$', DefaultFormByFieldView.as_view(), name='form_by_field'),
    url(r'^form_horizontal$', FormHorizontalView.as_view(), name='form_horizontal'),
    url(r'^form_inline$', FormInlineView.as_view(), name='form_inline'),
    url(r'^form_with_files$', FormWithFilesView.as_view(), name='form_with_files'),
    url(r'^pagination$', PaginationView.as_view(), name='pagination'),
    url(r'^misc$', MiscView.as_view(), name='misc'),
]
