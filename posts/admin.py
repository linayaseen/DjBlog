from django.contrib import admin

# Register your models here.
from.models import Post

class ProductAdmin(admin.ModelAdmin):
    list_display=['title','draft']
    list_filter=['draft']
    search_fields=['title']

admin.site.register(Post,ProductAdmin)