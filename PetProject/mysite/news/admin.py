from django.contrib import admin

from .models import News, Category, Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created', 'updated_at', 'is_published')
    list_display_links = ('title', 'id')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'category')
    list_editable = ('is_published',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title', 'id')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)