from django.contrib import admin
from .models import *


class AboutUsImageInLine(admin.TabularInline):
    model = AboutUsImage
    max_num = 3
    min_num = 3


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsImageInLine, ]
    list_display = ('title', 'text')

    def has_add_permission(self, request):
        return False if AboutUs.objects.all() else True


class ProductImageColorInLine(admin.TabularInline):
    model = ProductImageColor
    max_num = 8
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageColorInLine, ]
    list_display = ('collection', 'title', 'article', 'old_price', 'discount', 'new_price',
                    'description', 'line_of_size', 'compound', 'amount', 'material', 'new',
                    'hit')
    list_filter = ('hit', 'new')
    search_fields = ("title__startswith",)



class NumberInLine(admin.TabularInline):
    model = Number
    max_num = 2
    min_num = 1


@admin.register(SecondFooter)
class SecondFooterAdmin(admin.ModelAdmin):
    inlines = [NumberInLine, ]
    list_display = ('messen', 'link')

    def has_add_permission(self, request):
        return False if SecondFooter.objects.all() else True


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('imformation', 'number', 'logo')

    def has_add_permission(self, request):
        return False if Footer.objects.all() else True


@admin.register(Oferro)
class OferroAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    def has_add_permission(self, request):
        return False if Oferro.objects.all() else True


@admin.register(ImageHelp)
class ImageHelpAdmin(admin.ModelAdmin):
    list_display = (str('image'),)

    def has_add_permission(self, request):
        return False if ImageHelp.objects.all() else True


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon')


@admin.register(News)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')



@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


admin.site.register(Slider)
admin.site.register(BackCall)
admin.site.register(User)
