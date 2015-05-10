from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# customize admin view for Question
class QuestionAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,                  {'fields':['question_text']}),
        ('Date Information',    {'fields':['pub_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInline]

    # fields to display when the list of records is shown
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # add a "Filter" sidebar to let users filter the change by pub_date
    list_filter = ['pub_date']

    # search capability
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)  








