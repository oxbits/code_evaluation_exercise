from django.contrib import admin
from .models import (
    QuestionSet,
    Question,
    Answer,
    Image,
)


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    ordering = ("order",)


class QuestionSetAdmin(admin.ModelAdmin):
    inlines = [
        QuestionInline,
    ]
    

admin.site.register(QuestionSet, QuestionSetAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Image)

