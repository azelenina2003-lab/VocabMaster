from django.contrib import admin
from .models import Category, Entry

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('term', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('term', 'definition')