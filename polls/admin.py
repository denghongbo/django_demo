from django.contrib import admin
from .models import Question, Choice
from django import forms
from django.contrib.admin.views.main import ChangeList
from ajax_select.fields import AutoCompleteSelectField
from django.core.paginator import EmptyPage, InvalidPage, Paginator


class InlineChangeList(object):
    can_show_all = True
    multi_page = True
    get_query_string = ChangeList.__dict__['get_query_string']

    def __init__(self, request, page_num, paginator):
        self.show_all = 'all' in request.GET
        self.page_num = page_num
        self.paginator = paginator
        self.result_count = paginator.count
        self.params = dict(request.GET.items())


class PaginationInline(admin.TabularInline):
    template = 'admin/edit_inline/tabular_paginated.html'
    per_page = 20

    def get_formset(self, request, obj=None, **kwargs):
        formset_class = super(PaginationInline, self).get_formset(
            request, obj, **kwargs)

        class PaginationFormSet(formset_class):
            def __init__(self, *args, **kwargs):
                super(PaginationFormSet, self).__init__(*args, **kwargs)

                qs = self.queryset
                paginator = Paginator(qs, self.per_page)
                try:
                    page_num = int(request.GET.get('p', '0'))
                except ValueError:
                    page_num = 0

                try:
                    page = paginator.page(page_num + 1)
                except (EmptyPage, InvalidPage):
                    page = paginator.page(paginator.num_pages)

                self.cl = InlineChangeList(request, page_num, paginator)
                self.paginator = paginator

                if self.cl.show_all:
                    self._queryset = qs
                else:
                    self._queryset = page.object_list

        PaginationFormSet.per_page = self.per_page
        return PaginationFormSet


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


def votes_set_one(modeladmin, request, queryset):
    queryset.update(votes='1')


votes_set_one.short_description = "Set Votes To One"


class ChoiceForm(forms.ModelForm):
    choice_text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 15,
        'cols': 100,
        'class': 'materialize-textarea',
    }))
    question = AutoCompleteSelectField('questions')


class ChoiceAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ('choice_text', 'votes')
    actions = [votes_set_one]
    form = ChoiceForm


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_per_page = 10
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
