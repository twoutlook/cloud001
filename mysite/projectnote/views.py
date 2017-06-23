# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages

# by Mark
from django.shortcuts import get_object_or_404, render, redirect

from .forms import ContactForm, FilesForm, ContactFormSet
from .models import Note
from django.db.models import Count,Max, Min, Sum, Avg

from .models import Flowchart
from .models import Flowchartprocess
from .models import Smm, Employee, Trans,Rpt,Sop,Sopitem, Dept, Sopdata, Drill, Prog, Drillstep,Dailywork

# 2017-03-20
# woring together with 盼盼 & 婷婷
from .models import Bpm

from .models import TechNote

from .models import T100Todo
from .models import TrackReport00


# from .models import T100Todo2



# 2017-04-06
from .models import SqlStatement


def index(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')

    # http://stackoverflow.com/questions/4577513/how-do-i-change-a-django-template-based-on-the-users-group
    # item001=get_object_or_404(Item001, pk=item001_id)
    is_grp001=request.user.groups.filter(name='grp001').exists()
    is_grp002=request.user.groups.filter(name='grp002').exists()
    is_grp003=request.user.groups.filter(name='grp003').exists()
    is_grp005=request.user.groups.filter(name='grp005').exists()

    item_list = Note.objects.order_by('date1')[:100]
    context = {'current_user':request.user,'page_title':'目錄','item_list': item_list,'is_grp001':is_grp001,
    'is_grp002':is_grp002,
    'is_grp003':is_grp003,
    'is_grp005':is_grp005

    }

    # context = {'current_user':request.user,'page_title':'TEST1︰'}
    return render(request, 'projectnote/index.html', context)


def test1(request):
    is_grp001=request.user.groups.filter(name='grp001').exists()
    if not is_grp001:
         return redirect('/projectnote')

    # item001=get_object_or_404(Item001, pk=item001_id)
    item_list = Note.objects.order_by('date1')[:100]
    context = {'current_user':request.user,'page_title':'實施記要','item_list': item_list}

    # context = {'current_user':request.user,'page_title':'TEST1︰'}
    return render(request, 'projectnote/test1.html', context)
def test2(request):
    is_grp001=request.user.groups.filter(name='grp001').exists()
    if not is_grp001:
         return redirect('/projectnote')

    # item001=get_object_or_404(Item001, pk=item001_id)
    item_list = Note.objects.order_by('date1')[:100]
    context = {'current_user':request.user,'page_title':'TEST2','item_list': item_list}

    # context = {'current_user':request.user,'page_title':'TEST1︰'}
    return render(request, 'projectnote/test1.html', context)

# http://yuji.wordpress.com/2013/01/30/django-form-field-in-initial-data-requires-a-fieldfile-instance/
class FakeField(object):
    storage = default_storage


fieldfile = FieldFile(None, FakeField, 'dummy.txt')


class HomePageView(TemplateView):
    template_name = 'projectnote/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        messages.info(self.request, 'hello http://example.com')
        return context


class DefaultFormsetView(FormView):
    template_name = 'projectnote/formset.html'
    form_class = ContactFormSet


class DefaultFormView(FormView):
    template_name = 'projectnote/form.html'
    form_class = ContactForm


class DefaultFormByFieldView(FormView):
    template_name = 'projectnote/form_by_field.html'
    form_class = ContactForm


class FormHorizontalView(FormView):
    template_name = 'projectnote/form_horizontal.html'
    form_class = ContactForm


class FormInlineView(FormView):
    template_name = 'projectnote/form_inline.html'
    form_class = ContactForm


class FormWithFilesView(FormView):
    template_name = 'projectnote/form_with_files.html'
    form_class = FilesForm

    def get_context_data(self, **kwargs):
        context = super(FormWithFilesView, self).get_context_data(**kwargs)
        context['layout'] = self.request.GET.get('layout', 'vertical')
        return context

    def get_initial(self):
        return {
            'file4': fieldfile,
        }


class PaginationView(TemplateView):
    template_name = 'projectnote/pagination.html'

    def get_context_data(self, **kwargs):
        context = super(PaginationView, self).get_context_data(**kwargs)
        lines = []
        for i in range(200):
            lines.append('Line %s' % (i + 1))
        paginator = Paginator(lines, 10)
        page = self.request.GET.get('page')
        try:
            show_lines = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            show_lines = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            show_lines = paginator.page(paginator.num_pages)
        context['lines'] = show_lines
        return context


class MiscView(TemplateView):
    template_name = 'projectnote/misc.html'

# SECTION , by MARK
def p1(request):
    if not request.user.is_authenticated:
        #  return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        context = {'page_title':'您現在訪問 APP001，但是還沒有登入','item_list': {}}
        return render(request, 'P/index.html', context)

    item_list = Flowchartprocess.objects.all()

    context = {'current_user':request.user,'page_title':'xxx','item_list': item_list}
    return render(request, 'projectnote/p1.html', context)

def flowchart_list(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    is_grp002=request.user.groups.filter(name='grp002').exists()
    if not is_grp002:
         return redirect('/projectnote')
    # 总平均价
    item_list = Flowchart.objects.order_by('part_name', 'id')[:3000]

    context = {'current_user':request.user,'page_title':'生产工艺流程卡','item_list':item_list}
    return render(request, 'projectnote/flowchart_list.html', context)



def flowchart(request,item_id):
    is_grp002=request.user.groups.filter(name='grp002').exists()
    if not is_grp002:
         return redirect('/projectnote')

    item=get_object_or_404(Flowchart, pk=item_id)
    itemprocess=Flowchartprocess.objects.filter(flowchart = item_id)

    context = {'current_user':request.user,'page_title':'生产工艺流程卡 - '+item.part_name,'item': item,'itemprocess': itemprocess}
    return render(request, 'projectnote/flowchart.html', context)
def smm(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'byquarter': byquarter}
    return render(request, 'materialprice/smm.html', context)



item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
bydesignation=Smm.objects.values('designation').annotate(date_from=Min('pricedate'), date_to=Max('pricedate'), date_cnt=Count('pricedate'))
avgbymonth=Smm.objects.values('yearnum','monthnum','designation').annotate(avg=Avg('priceavg')/1000)
bymonthcheck=Smm.objects.values('yearnum','monthnum','designation').annotate(cnt=Count('designation'))
byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)


def step0(request):
    # 2016-12-02, by WuNan
    # 按 step3 照做

    is_grp003=request.user.groups.filter(name='grp003').exists()
    if not is_grp003:
         return redirect('/projectnote')
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user
    ,'page_title':'STEP 0'
    ,'item_list': item_list
    ,'subtotal': subtotal
    ,'byquarter': byquarter
    ,'bydesignation': bydesignation
    }
    return render(request, 'projectnote/step0.html', context)
def step1(request):
    # 2016-12-02, by WuNan
    # 按 step3 照做

    is_grp003=request.user.groups.filter(name='grp003').exists()
    if not is_grp003:
         return redirect('/projectnote')
    item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    # subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    # byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'bymonth': bymonth,'bymonthcheck': bymonthcheck}
    return render(request, 'projectnote/step1.html', context)

def employee(request):
    # 2016-12-02, by WuNan
    # 按 step3 照做

    is_grp=request.user.groups.filter(name='grp002').exists()
    if not is_grp:
         return redirect('/projectnote')

    item_list = Employee.objects.order_by('c', 'd', 'e', 'a')[:3000]
    subtotal=Employee.objects.values('c', 'd','e').annotate(cnt=Count('a'))
    sub1=Employee.objects.values('c', 'd').annotate(cnt=Count('a'))
    sub0=Employee.objects.values('c').annotate(cnt=Count('a'))
    # byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)

    context = {'current_user':request.user,'page_title':'Employee',
    'item_list': item_list,
    'sub0': sub0,
    'sub1': sub1,

    'subtotal': subtotal,

    # 'byquarter': byquarter
    }
    return render(request, 'projectnote/employee.html', context)

def employeev2(request):
    # 2016-12-02, by WuNan
    # 按 step3 照做

    is_grp=request.user.groups.filter(name='grp002').exists()
    if not is_grp:
         return redirect('/projectnote')

    item_list = Employee.objects.order_by('c', 'd', 'e', 'a')[:3000]
    subtotal=Employee.objects.values('c', 'd','e').annotate(cnt=Count('a'))
    sub1=Employee.objects.values('c', 'd').annotate(cnt=Count('a'))
    sub0=Employee.objects.values('c').annotate(cnt=Count('a'))
    # byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)

    context = {'current_user':request.user,'page_title':'Employee',
    'item_list': item_list,
    'sub0': sub0,
    'sub1': sub1,

    'subtotal': subtotal,

    # 'byquarter': byquarter
    }
    return render(request, 'projectnote/employeev2.html', context)


def trans(request):
    # 2016-12-02, by WuNan
    # 按 step3 照做

    is_grp=request.user.groups.filter(name='grp002').exists()
    if not is_grp:
         return redirect('/projectnote')

    item_list = Trans.objects.order_by('a', 'b', 'f')[:3000]
    sub1=Trans.objects.values('yrmonth', 'd','e').annotate(sum=Sum('f'))
    subtotal=Trans.objects.values('yrmonth','cat', 'd','e').annotate(sum=Sum('f'))
    # sub1=Employee.objects.values('c', 'd').annotate(cnt=Count('a'))
    # sub0=Employee.objects.values('c').annotate(cnt=Count('a'))
    # # byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)

    context = {'current_user':request.user,'page_title':'收发存统计表-原材料',
    'item_list': item_list,
    # 'sub0': sub0,
    'sub1': sub1,

    'subtotal': subtotal,

    # 'byquarter': byquarter
    }
    return render(request, 'projectnote/trans.html', context)

def rpt(request):
    # 2016-12-02, by WuNan
    # 按 step3 照做

    is_grp=request.user.groups.filter(name='grp002').exists()
    if not is_grp:
         return redirect('/projectnote')

    item_list = Rpt.objects.order_by('yrmonth','a', 'b')[:3000]
    # sub1=Trans.objects.values('yrmonth', 'd','e').annotate(sum=Sum('f'))
    # subtotal=Trans.objects.values('yrmonth','cat', 'd','e').annotate(sum=Sum('f'))
    # sub1=Employee.objects.values('c', 'd').annotate(cnt=Count('a'))
    # sub0=Employee.objects.values('c').annotate(cnt=Count('a'))
    # # byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)

    context = {'current_user':request.user,'page_title':'收发存统计表-原材料(V2)',
    'item_list': item_list,
    # 'sub0': sub0,


    # 'byquarter': byquarter
    }
    return render(request, 'projectnote/rpt.html', context)


def rptdetail(request,item001_id):
    # 2016-12-02, by WuNan
    # 按 step3 照做

    is_grp=request.user.groups.filter(name='grp002').exists()
    if not is_grp:
         return redirect('/projectnote')

    item_list = Rpt.objects.order_by('yrmonth','a', 'b')[:3000]
    item_list2 = Rpt.objects.filter(yrmonth=item001_id).order_by('yrmonth','a', 'b')[:3000]


    # sub1=Trans.objects.values('yrmonth', 'd','e').annotate(sum=Sum('f'))
    # subtotal=Trans.objects.values('yrmonth','cat', 'd','e').annotate(sum=Sum('f'))
    # sub1=Employee.objects.values('c', 'd').annotate(cnt=Count('a'))
    # sub0=Employee.objects.values('c').annotate(cnt=Count('a'))
    # # byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)

    context = {'current_user':request.user,'page_title':'收发存统计表-原材料(V2)',
    'item_list': item_list,
    'item_list2': item_list2,

    # 'sub0': sub0,


    # 'byquarter': byquarter
    }
    return render(request, 'projectnote/rptdetail.html', context)


def bymonth(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    # item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    # subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    # byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'avgbymonth': avgbymonth,'bymonthcheck': bymonthcheck}
    return render(request, 'projectnote/bymonth.html', context)


def step2(request):
    # 2016-12-02, by WuNan
    # 按 step3 照做

    is_grp003=request.user.groups.filter(name='grp003').exists()
    if not is_grp003:
         return redirect('/projectnote')

    item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'byquarter': byquarter}
    return render(request, 'projectnote/step2.html', context)

def step3(request):
    # 2016-12-02, by Mark
    # 只允許具有 grp001 群組的用戶可以訪問
    # 否則頁面轉到全制程追踪系統的目錄

    # 2016-12-02, by Mark
    # 拆分 grp001 為 grp001 grp002 grp003
    is_grp003=request.user.groups.filter(name='grp003').exists()
    if not is_grp003:
         return redirect('/projectnote')

    item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    datacheck1=Smm.objects.values('designation').annotate(min=Min('pricedate'),max=Max('pricedate'),cnt=Count('pricedate'),)
    datacheck2=Smm.objects.values('designation', 'yearnum','monthnum').annotate(cnt=Count('priceavg'))
    subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,
        'page_title':'SMM',
        'item_list': item_list,
        'subtotal': subtotal,
        'byquarter': byquarter,
        'datacheck1':datacheck1,
        'datacheck2':datacheck2,
    }
    return render(request, 'projectnote/step3.html', context)


def step3ext(request,item_id):
    # 2016-12-02, by Mark
    # 只允許具有 grp001 群組的用戶可以訪問
    # 否則頁面轉到全制程追踪系統的目錄

    is_grp003=request.user.groups.filter(name='grp003').exists()
    if not is_grp003:
         return redirect('/projectnote')
# http://stackoverflow.com/questions/6102127/django-model-filter-on-date-ranges
    # MyModel.objects.filter(date__range=(range_start, range_end))
    # http://stackoverflow.com/questions/4668619/django-database-query-how-to-filter-objects-by-date-range
    datacheck3=Smm.objects.filter(pricedate__range = ["2016-01-01", item_id]).values( 'yearnum','monthnum').annotate(cnt=Count('priceavg'))



    item_list = Smm.objects.filter(pricedate__range = ["2016-01-01", item_id]).order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    # date_time_field__contains=datetime.date(1986, 7, 28)
    datacheck1=Smm.objects.filter(pricedate__range = ["2016-01-01", item_id]).values('designation').annotate(min=Min('pricedate'),max=Max('pricedate'),cnt=Count('pricedate'),)
    datacheck2=Smm.objects.filter(pricedate__range = ["2016-01-01", item_id]).values('designation', 'yearnum','monthnum').annotate(cnt=Count('priceavg'))
    subtotal=Smm.objects.filter(pricedate__range = ["2016-01-01", item_id]).values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    byquarter=Smm.objects.filter(pricedate__range = ["2016-01-01", item_id]).values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,
        'page_title':'SMM',
        'item_list': item_list,
        'subtotal': subtotal,
        'byquarter': byquarter,
        'datacheck1':datacheck1,
        'datacheck2':datacheck2,
        'datacheck3':datacheck3,
        'enddate':item_id,

    }
    return render(request, 'projectnote/step3ext.html', context)



def step3a(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    # item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    # subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    # byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'avgbymonth': avgbymonth,'bymonthcheck': bymonthcheck}
    return render(request, 'projectnote/bymonth.html', context)

# SOP
def sop(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    # item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    # TO SHOW ALL , INCLUDING ACTIVE OR NOT
    item_list = Sop.objects.order_by('code')[:500]

    context = {'item_list': item_list}
    return render(request, 'projectnote/sop_list.html', context)

def t100_report_list(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    # item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    # TO SHOW ALL , INCLUDING ACTIVE OR NOT
    item_list = TrackReport00.objects.order_by('dept','a')[:1500]

    context = {'item_list': item_list}
    return render(request, 'projectnote/t100_report_list.html', context)



def dailywork(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    # item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    # TO SHOW ALL , INCLUDING ACTIVE OR NOT
    item_list = Dailywork.objects.order_by('empe_name','work_date')[:500]

    context = {'item_list': item_list}
    return render(request, 'projectnote/dailywork_list.html', context)

# 2017-03-20
# woring together with 盼盼 & 婷婷
def bpm(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Bpm.objects.order_by('dept_name','sop_name')[:500]

    context = {'item_list': item_list}
    return render(request, 'projectnote/bpm_list.html', context)

def technote(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    ip_list = TechNote.objects.filter(a='开发者服务器')
    item_list = TechNote.objects.order_by('a','b')[:500]

    context = {'item_list': item_list,'ip_list': ip_list}
    return render(request, 'projectnote/technote_list.html', context)


def t100todo(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    # if not is_grpxxx:
    #    return redirect('/projectnote')

    # ip_list = TechNote.objects.filter(a='开发者服务器')
    item_list = T100Todo.objects.order_by('a')[:500]

    context = {'item_list': item_list}
    return render(request, 'projectnote/t100todo_list.html', context)

# def t100todo2(request):
#     is_grpxxx=request.user.groups.filter(name='grp005').exists()
#     if not is_grpxxx:
#        return redirect('/projectnote')
#
#     # ip_list = TechNote.objects.filter(a='开发者服务器')
#     item_list = T100Todo2.objects.order_by('a')[:500]
#
#     context = {'item_list': item_list}
#     return render(request, 'projectnote/t100todo2_list.html', context)



def bpm2(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Bpm.objects.filter(bpm_type='T100送签').order_by('dept_name','sop_name')[:500]

    context = {'item_list': item_list}
    return render(request, 'projectnote/bpm_list.html', context)

# 2017-03-22
# bpm4
# (1) view.py, def bpm3(request):
# (2) projectnote/bpm_list3.html
# (3) urls.py, url(r'^bpm3$', views.bpm3, name='bpm3'),
# (4)在index加按钮
def bpm4(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Bpm.objects.filter(dept_name='人事').order_by('dept_name','sop_name')[:500]

    context = {'item_list': item_list}
    return render(request, 'projectnote/bpm_list4.html', context)
def bpm3(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Bpm.objects.filter(bpm_type='纯BPM').order_by('dept_name','sop_name')[:500]

    context = {'item_list': item_list}
    return render(request, 'projectnote/bpm_list3.html', context)


def initdata(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    # item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    # TO SHOW ALL , INCLUDING ACTIVE OR NOT
    item_list = Sopdata.objects.order_by('cat','seq')[:500]

    context = {'item_list': item_list}
    return render(request, 'projectnote/initdata.html', context)
def initdata2(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    # item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    # TO SHOW ALL , INCLUDING ACTIVE OR NOT
    item_list = Sopdata.objects.order_by('cat','seq')[:500]

    context = {'item_list': item_list}
    return render(request, 'projectnote/initdata2.html', context)

def initdata_yn(request, is_required):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    # item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    # TO SHOW ALL , INCLUDING ACTIVE OR NOT
    # item_list = Sopdata.objects.order_by('cat','seq')[:500]
    if is_required == 'y':
        item_list = Sopdata.objects.filter(is_required = True).order_by('cat','seq')[:500]
    if is_required == 'n':
        item_list = Sopdata.objects.filter(is_required = False).order_by('cat','seq')[:500]


    context = {'item_list': item_list}
    return render(request, 'projectnote/initdata_yn.html', context)

def sopdept(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    # item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    # TO SHOW ALL , INCLUDING ACTIVE OR NOT
    item_list = Dept.objects.order_by('order_seq')[:500]

    context = {'item_list': item_list}
    return render(request, 'projectnote/sop_dept.html', context)



def sop2(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    context = {'item_list': item_list}
    return render(request, 'projectnote/sop_list2.html', context)
def sop3(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    context = {'item_list': item_list}
    return render(request, 'projectnote/sop_list3.html', context)
def sop4(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    context = {'item_list': item_list}
    return render(request, 'projectnote/sop_list4.html', context)

def sopdept_selected(request,dept_id):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Sop.objects.filter(dept2 = dept_id).order_by('code')[:500]
    dept = Dept.objects.filter(id = dept_id)

    context = {'item_list': item_list, 'dept':dept}
    return render(request, 'projectnote/sopdept_selected.html', context)

def drill_list(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Drill.objects.order_by('code')[:500]
    # dept = Dept.objects.filter(id = dept_id)

    # context = {'item_list': item_list, 'dept':dept}
    context = {'item_list': item_list}

    return render(request, 'projectnote/drill_list.html', context)


def drill_selected(request,dept_id):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Drill.objects.filter(id = dept_id).order_by('code')[:500]
    # dept = Dept.objects.filter(id = dept_id)

    # context = {'item_list': item_list, 'dept':dept}
    context = {'item_list': item_list}

    return render(request, 'projectnote/drill_selected.html', context)

def drill_selected2(request,dept_id):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Drill.objects.filter(id = dept_id).order_by('code')[:500]
    item_list2 = Drillstep.objects.filter(drill_id = dept_id).order_by('seq')[:500]
    # dept = Dept.objects.filter(id = dept_id)

    # context = {'item_list': item_list, 'dept':dept}
    context = {'item_list': item_list,'item_list2': item_list2}

    return render(request, 'projectnote/drill_selected2.html', context)


def sopbpm(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Sop.objects.filter(is_bpm = True).order_by('code')[:500]
    context = {'item_list': item_list}
    return render(request, 'projectnote/sop_list_bpm.html', context)


def js(request):
    # is_grpxxx=request.user.groups.filter(name='grp005').exists()
    # if not is_grpxxx:
    #    return redirect('/projectnote')

    # item_list = Sop.objects.filter(is_bpm = True).order_by('code')[:500]
    # context = {'item_list': item_list}

    item_list = SqlStatement.objects.filter(prj = 'monitor001').order_by('prj','seq')[:500]
    context = {'item_list': item_list}
    # context = {'item_list': "testing"}

    # return render(request, 'projectnote/js.html', context)
    return render(request, 'projectnote/js.js', context)

def js2(request):
    # is_grpxxx=request.user.groups.filter(name='grp005').exists()
    # if not is_grpxxx:
    #    return redirect('/projectnote')

    # item_list = Sop.objects.filter(is_bpm = True).order_by('code')[:500]
    # context = {'item_list': item_list}

    item_list = SqlStatement.objects.filter(prj = 'monitor001').filter(is_active=True).order_by('prj','seq')[:500]
    context = {'item_list': item_list}
    # context = {'item_list': "testing"}

    # return render(request, 'projectnote/js.html', context)
    return render(request, 'projectnote/js2.js', context)


def sopnotactive(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    item_list = Sop.objects.filter(is_active = False).order_by('code')[:500]
    context = {'item_list': item_list}
    return render(request, 'projectnote/sop_list_not_active.html', context)


def sop_detail(request, sop_id):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')
    sop = get_object_or_404(Sop, pk=sop_id)
    return render(request, 'projectnote/sop_detail.html', {'sop': sop})

def sop_detail_v2(request, sop_id):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    sop = get_object_or_404(Sop, pk=sop_id)
    return render(request, 'projectnote/sop_detail_v2.html', {'sop': sop})

def sop_detail_v3(request, sop_code):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    sop = get_object_or_404(Sop, code=sop_code)
    return render(request, 'projectnote/sop_detail_v2.html', {'sop': sop})


def sopitem(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    # sop = get_object_or_404(Sop, pk=sop_id)
    item_list = Sopitem.objects.order_by('sop','itemseq',)[:500]

    return render(request, 'projectnote/sopitem.html', {'item_list': item_list})

def sopcat(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    # item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    # TO SHOW ALL , INCLUDING ACTIVE OR NOT
    item_list = Sop.objects.order_by('code')[:500]
    cat_cnt=Sop.objects.order_by('dept','cat').values('cat','dept').annotate(cnt=Count('code'))

    context = {'item_list': item_list,'cat_cnt':cat_cnt}
    return render(request, 'projectnote/sop_cat.html', context)

def sopcat2(request):
    is_grpxxx=request.user.groups.filter(name='grp005').exists()
    if not is_grpxxx:
       return redirect('/projectnote')

    # item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    # TO SHOW ALL , INCLUDING ACTIVE OR NOT
    item_list = Sop.objects.order_by('code')[:500]
    cat_cnt=Sop.objects.order_by('dept2','cat2').values('cat2','dept2').annotate(cnt=Count('code'))

    context = {'item_list': item_list,'cat_cnt':cat_cnt}
    return render(request, 'projectnote/sop_cat2.html', context)
