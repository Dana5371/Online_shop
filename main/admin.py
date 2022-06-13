from django.contrib import admin
from .models import *

class AboutUsImageInLine(admin.TabularInline):
    model = AboutUsImage
    max_num = 3
    min_num = 3

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsImageInLine, ]



class ProductImageColorInLine(admin.TabularInline):
    model = ProductImageColor
    max_num = 8
    min_num = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageColorInLine, ]


class NumberInLine(admin.TabularInline):
    model = Number
    max_num = 2
    min_num = 1

@admin.register(SecondFooter)
class SecondFooterAdmin(admin.ModelAdmin):
    inlines = [NumberInLine, ]

admin.site.register(Footer)
admin.site.register(Benefit)
admin.site.register(News)
admin.site.register(Oferro)
admin.site.register(ImageHelp)
admin.site.register(Help)
admin.site.register(Collection)
admin.site.register(Slider)
admin.site.register(BackCall)
admin.site.register(User)




