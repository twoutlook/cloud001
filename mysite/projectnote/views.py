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
from .models import Smm

def index(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')

    # http://stackoverflow.com/questions/4577513/how-do-i-change-a-django-template-based-on-the-users-group
    # item001=get_object_or_404(Item001, pk=item001_id)
    is_grp001=request.user.groups.filter(name='grp001').exists()
    item_list = Note.objects.order_by('date1')[:100]
    context = {'current_user':request.user,'page_title':'目錄','item_list': item_list,'is_grp001':is_grp001}

    # context = {'current_user':request.user,'page_title':'TEST1︰'}
    return render(request, 'projectnote/index.html', context)


def test1(request):
    is_grp001=request.user.groups.filter(name='grp001').exists()
    if not is_grp001:
         return redirect('/projectnote')

    # item001=get_object_or_404(Item001, pk=item001_id)
    item_list = Note.objects.order_by('date1')[:100]
    context = {'current_user':request.user,'page_title':'TEST1','item_list': item_list}

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
    if not request.user.is_authenticated:
         return redirect('/')
    # 总平均价
    item_list = Flowchart.objects.order_by('part_name', 'id')[:3000]

    context = {'current_user':request.user,'page_title':'生产工艺流程卡','item_list':item_list}
    return render(request, 'projectnote/flowchart_list.html', context)



def flowchart(request,item_id):
    if not request.user.is_authenticated:
        return redirect('/')
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
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
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
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    # item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    # subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    # byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'bymonth': bymonth,'bymonthcheck': bymonthcheck}
    return render(request, 'projectnote/step1.html', context)

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
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'byquarter': byquarter}
    return render(request, 'projectnote/step2.html', context)
def step3(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')
    # 总平均价
    item_list = Smm.objects.order_by('designation', 'pricedate')[:3000]
    # subtotal =Receiving.objects.values("").annotate(Count('FG')).
    subtotal=Smm.objects.values('designation', 'yearnum','monthnum').annotate(avg=Avg('priceavg')/1000)
    byquarter=Smm.objects.values('designation', 'yearnum','quarternum').annotate(avg=Avg('priceavg')/1000)
    # item_list = Materialprice.objects.filter(materialprice__pricedate=='总平均价').order_by('designation', 'num')[:3000]

    context = {'current_user':request.user,'page_title':'SMM','item_list': item_list,'subtotal': subtotal,'byquarter': byquarter}
    return render(request, 'projectnote/step3.html', context)
