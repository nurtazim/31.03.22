# from django.contrib import admin
#
# from .models import Category, Product, Subcategory
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name']
#
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'price', 'stock', 'available']
#     list_filter = ['available', 'category']
#     list_editable = ['price', 'stock', 'available']
#
#
# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Subcategory)

from django.contrib import admin
from django.utils.safestring import mark_safe
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["get_image", 'title', 'price', 'stock', 'available', ]
    readonly_fields = ("get_image",)

    list_filter = ['available', 'category']
    list_editable = ['price', 'stock', 'available', ]

    def get_image(self, obj):
        try:
            return mark_safe(f'<img src={obj.image.url} width="100"')
        except:
            return ""

    get_image.short_description = "Изображение"


class CategoryAdmin(DjangoMpttAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
