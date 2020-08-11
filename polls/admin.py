from django.contrib import admin
from .models import Question, Choice
from django import forms
from ajax_select.fields import AutoCompleteSelectField


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
