from django.contrib import admin
from .models import Post_table
# Register your models here.

# Editing the Admin pannel
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    search_fields = ['title','content']     # includes search box
    list_display_links = ['date','title']


admin.site.register(Post_table,PostAdmin)
