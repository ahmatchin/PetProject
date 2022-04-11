from django.db import models

from django.urls import reverse_lazy


class News(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Содержимое')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to="photos/%Y/%M/%D/", verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='В наличии')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse_lazy('view_more', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'товарную позицию'
        verbose_name_plural = 'Добавить товарную позицию'
        ordering = ['-created']


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категории товаров')

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Катерория товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ['title']


class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Введите имя')
    text = models.TextField(max_length=1000, verbose_name='Введите комментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['name']
