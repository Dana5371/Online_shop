from django.contrib import admin
from .models import *


class AboutUsImageInLine(admin.TabularInline):
    model = AboutUsImage
    max_num = 3
    min_num = 3


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsImageInLine, ]

    def has_add_permission(self, request):
        return False if AboutUs.objects.all() else True


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

    def has_add_permission(self, request):
        return False if SecondFooter.objects.all() else True


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if Footer.objects.all() else True

@admin.register(Oferro)
class OferroAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if Oferro.objects.all() else True

@admin.register(ImageHelp)
class ImageHelpAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if ImageHelp.objects.all() else True


admin.site.register(Benefit)
admin.site.register(News)
admin.site.register(Help)
admin.site.register(Collection)
admin.site.register(Slider)
admin.site.register(BackCall)
admin.site.register(User)

