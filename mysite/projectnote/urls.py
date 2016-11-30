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
    url(r'^p1$', views.test1, name='p1'),
    url(r'^flowchart$', views.flowchart, name='flowchart'),
    url(r'^flowchart_list$', views.flowchart_list, name='flowchart_list'),

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
