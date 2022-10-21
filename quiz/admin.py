from django.contrib import admin
from .models import Quiz, Question, Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
   inlines = [ChoiceInline, ]
   

admin.site.register(Question, QuestionAdmin)
admin.site.register(Quiz)
# admin.site.register(Choice)
# admin.site.register(Question)
# admin.site.register(Quiz)

