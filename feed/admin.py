from django.contrib import admin

from feed.models import User, Post, PostImage, Comment, Like, Repost

admin.site.register(User)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Repost)
