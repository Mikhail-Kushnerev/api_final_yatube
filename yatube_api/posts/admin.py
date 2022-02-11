from django.contrib import admin

from .models import Post, Group, Comment, Follow
# Register your models here.
@admin.register(Post)
class PostwAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'author',
        'text',
        'group',
        'image'
    )
    empty_value_display = '-пусто-'

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'description'
    )
    empty_value_display = '-пусто-'

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'following')
    empty_value_display = '-пусто-'