from django.contrib import admin
from .models import Todo_List

# Register your models here.

class TodoListAdmin(admin.ModelAdmin):
    list_display = ('no', 'pcode', 'user_id', 'title', 'content', 'is_complete')

admin.site.register(Todo_List, TodoListAdmin)

