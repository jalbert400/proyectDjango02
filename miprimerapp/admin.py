from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('title','created','publish','author')
    search_fields = ('title','body')
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    prepopulated_fields = {'slug':('title',)}

# Register your models here.
admin.site.register(Post,PostAdmin)