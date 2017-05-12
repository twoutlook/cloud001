# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import HomePageView, FormHorizontalView, FormInlineView, PaginationView, FormWithFilesView, \
    DefaultFormView, MiscView, DefaultFormsetView, DefaultFormByFieldView

# by Mark
from . import views

urlpatterns = [
    # url(r'^bpm$', views.bpm, name='bpm'),
    

    # 2017-04-05 
    # by Mark, 希望能在django的環境提供SQL的語句甚至智能維護下拉的內容.
    url(r'^js$', views.js, name='js'),
    url(r'^js2$', views.js2, name='js2'),
    

    url(r'^technote$', views.technote, name='technote'),
    

    # 2017-03-20 
    # woring together with 盼盼 & 婷婷
    url(r'^bpm$', views.bpm, name='bpm'),

    url(r'^bpm2$', views.bpm2, name='bpm2'),
    url(r'^bpm3$', views.bpm3, name='bpm3'),
    url(r'^bpm4$', views.bpm4, name='bpm4'),
    
    url(r'^dailywork$', views.dailywork, name='dailywork'),
    

    url(r'^sop$', views.sop, name='sop'),

    url(r'^initdata$', views.initdata, name='initdata'),
    url(r'^initdata2$', views.initdata2, name='initdata2'),
    url(r'^initdata/(?P<is_required>[yn])/$', views.initdata_yn, name='initdata_yn'),
    url(r'^sopcat$', views.sopcat, name='sopcat'),
    url(r'^sopcat2$', views.sopcat2, name='sopcat2'),
    url(r'^sop2$', views.sop2, name='sop2'),
    url(r'^sop3$', views.sop3, name='sop3'),
    url(r'^sop4$', views.sop4, name='sop4'),
    url(r'^sopbpm$', views.sopbpm, name='sopbpm'),
    url(r'^sopdept$', views.sopdept, name='sopdept'),
    url(r'^sopnotactive$', views.sopnotactive, name='sopnotactive'),
    url(r'^sop/(?P<sop_id>[0-9]+)/$', views.sop_detail, name='sop_detail'),
    
    url(r'^sop/format2/(?P<sop_id>[0-9]+)/$', views.sop_detail_v2, name='sop_detail_v2'),
    url(r'^sop/format3/(?P<sop_code>[A-Z0-9]+)/$', views.sop_detail_v3, name='sop_detail_v3'),
    
    url(r'^sopdept/(?P<dept_id>[0-9]+)/$', views.sopdept_selected, name='sopdept_selected'),
    url(r'^drill/(?P<dept_id>[0-9]+)/$', views.drill_selected, name='drill_selected'),
    # url(r'^drill2/(?P<dept_id>[0-9]+)/$', views.drill_selected2, name='drill_selected2'),
    url(r'^drilllist$', views.drill_list, name='drill_list'),




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
    url(r'^rpt$', views.rpt, name='rpt'),
    url(r'^rpt/(?P<item001_id>[_A-Za-z0-9-\\+]+)', views.rptdetail, name='rptdetail'), #item001/123 後面有東西都好
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
