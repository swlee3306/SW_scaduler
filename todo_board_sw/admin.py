from django.contrib import admin
from .models import Todo_list

# Register your models here.

class TodoListAdmin(admin.ModelAdmin):
    list_display = ('no', 'pcode' , 'user_id','title', 'content','is_complete')

admin.site.register(Todo_list, TodoListAdmin)

