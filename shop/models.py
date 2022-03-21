from django.db import models
#
#
# def upload_to(instance, filename):
#     return f'{filename}'
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=250, verbose_name="Категория")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'
#
#
# class Subcategory(models.Model):
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200, verbose_name="Подкатегория")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Подкатегория'
#         verbose_name_plural = 'Подкатегория'
#
#
# class Product(models.Model):
#     subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория', null=True,
#                                     blank=True)
#     # category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
#     image = models.ImageField(upload_to=upload_to, verbose_name="Изображение")
#     title = models.TextField(max_length=100, null=True, verbose_name="Продукт")
#     descriptions = models.TextField(blank=True, verbose_name="Описание")
#     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
#     available = models.BooleanField(default=True, verbose_name="актуальность")
#     stock = models.PositiveIntegerField(verbose_name="Количество товара")
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "Продукт"
#         verbose_name_plural = 'Продукты'

from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


def upload_to(instance, filename):
    return f'{filename}'


class Product(models.Model):
    image = models.ImageField(upload_to=upload_to, verbose_name="Изображение")
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    available = models.BooleanField(default=True, verbose_name="актуальность")
    content = models.TextField(verbose_name='Содержание')
    stock = models.PositiveIntegerField(verbose_name="Количество товара")

    def __str__(self):
        return self.title

    class Meta:
        unique_together = [['category', 'slug']]
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title
