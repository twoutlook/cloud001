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


def test1(request):
    # if not request.user.is_authenticated:
    #      return redirect('/')

    # item001=get_object_or_404(Item001, pk=item001_id)
    item_list = Note.objects.order_by('id')[:100]
    context = {'current_user':request.user,'page_title':'APP001-雲端佈告欄','item_list': item_list}

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
