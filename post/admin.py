from django.contrib import admin

# Register your models here.
from .models import *


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'content', 'created', 'category')


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostModelAdmin)
