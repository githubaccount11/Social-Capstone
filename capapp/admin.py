from django.contrib import admin

from .models import Post, Comments, Images, Profile

admin.site.register(Comments)
admin.site.register(Post)
admin.site.register(Images)
admin.site.register(Profile)