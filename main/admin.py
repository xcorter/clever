from django.contrib import admin
from .models import Question, Choice, Game
import nested_admin


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    max_num = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    search_fields = ['question']
    list_display = ['id', 'question']

class ChoiceNestedInline(nested_admin.NestedStackedInline):
    model = Choice
    extra = 3
    max_num = 3

class QuestionStacked(nested_admin.NestedStackedInline):
    model = Question
    extra = 12
    max_num = 12
    inlines = [ChoiceNestedInline]

class GameAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionStacked]
    list_filter = ['date_time', 'leading']
    list_display = ['id', 'date_time', 'leading']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Game, GameAdmin)
