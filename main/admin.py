from django.contrib import admin
from .models import *

class AboutUsImageInLine(admin.TabularInline):
    model = AboutUsImage
    max_num = 3
    min_num = 3

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsImageInLine, ]

