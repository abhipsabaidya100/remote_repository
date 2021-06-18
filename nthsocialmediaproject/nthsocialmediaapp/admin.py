from django.contrib import admin

from .models import Post,Comments

class AdminPost(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=['title','slug','created','author','body']

admin.site.register(Post,AdminPost)
admin.site.register(Comments)
