from django.contrib import admin
from .models import *

class AboutUsImageInLine(admin.TabularInline):
    model = AboutUsImage
    max_num = 3
    min_num = 3

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsImageInLine, ]

admin.site.register(Benefit)
admin.site.register(News)
admin.site.register(Oferro)
admin.site.register(ImageHelp)

class AnswerInLine(admin.TabularInline):
    model = Answer
    max_num = 1
    min_num = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine, ]



