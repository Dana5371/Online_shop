from django.contrib import admin
from django.shortcuts import redirect

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

    def delete(self):
        return False

    def changelist_view(self, request, extra_context=None):
        if AboutUs.objects.all().first():
            aboutus = AboutUs.objects.all().first()
            return redirect(request.path + str(aboutus.id))
        elif AboutUs.objects.all().count() < 1:
            return redirect(request.path + 'add')


class ProductImageColorInLine(admin.TabularInline):
    model = ProductImageColor
    max_num = 8
    min_num = 1
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageColorInLine, ]
    list_display = ('collection', 'title', 'article', 'old_price',
                    'discount', 'new_price', 'line_of_size',
                    'compound', 'material', 'new', 'hit')
    list_filter = ('hit', 'new')
    search_fields = ("title__startswith",)


class SecondFooterInLine(admin.TabularInline):
    model = SecondFooter
    min_num = 1


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('imformation', 'number', 'logo')
    inlines = [SecondFooterInLine, ]

    def has_add_permission(self, request):
        return False if Footer.objects.all() else True

    def delete(self):
        return False

    def changelist_view(self, request, extra_context=None):
        if Footer.objects.all().first():
            footer = Footer.objects.all().first()
            return redirect(request.path + str(footer.id))
        elif Footer.objects.all().count() < 1:
            return redirect(request.path + 'add')


@admin.register(Oferro)
class OferroAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

    def has_add_permission(self, request):
        return False if Oferro.objects.all() else True

    def delete(self):
        return False

    def changelist_view(self, request, extra_context=None):
        if Oferro.objects.all().first():
            offer = Oferro.objects.all().first()
            return redirect(request.path + str(offer.id))
        elif Oferro.objects.all().count() < 1:
            return redirect(request.path + 'add')


@admin.register(ImageHelp)
class ImageHelpAdmin(admin.ModelAdmin):
    list_display = (str('image'),)

    def has_add_permission(self, request):
        return False if ImageHelp.objects.all() else True

    def delete(self):
        return False

    def changelist_view(self, request, extra_context=None):
        if ImageHelp.objects.all().first():
            image = ImageHelp.objects.all().first()
            return redirect(request.path + str(image.id))
        elif ImageHelp.objects.all().count() < 1:
            return redirect(request.path + 'add')


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


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('image', 'field_link')

    def has_add_permission(self, request):
        return False if Slider.objects.all() else True

    def delete(self):
        return False

    def changelist_view(self, request, extra_context=None):
        if Slider.objects.all().first():
            slider = Slider.objects.all().first()
            return redirect(request.path + str(slider.id))
        elif Slider.objects.all().count() < 1:
            return redirect(request.path + 'add')


@admin.register(BackCall)
class BackCallAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_of_phone',
                    'type', 'status', 'date_of_call')
