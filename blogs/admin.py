from django.contrib import admin
from .models import Category, Blog


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'category_slug': ('category_name',)}


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured', 'status',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)

