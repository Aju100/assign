from django.contrib import admin

from .models import Author,Post

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'status',
    )
admin.site.register(Author)
admin.site.register(Post,PostAdmin)