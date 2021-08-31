from django.contrib import admin

from .models import Choice, Log, Person, Question


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'votes')


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date', 'was_published_recently')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_filter = ['last_name']
    list_display = ('first_name', 'last_name', 'email')


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_filter = ['method']
    list_display = ('path', 'method')
