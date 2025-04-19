from django.contrib import admin
from .models import (
    Post,
    Group,
    Follow,
    Comment
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Group)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Follow)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    pass
