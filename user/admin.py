from django.contrib import admin

from user.models import GitUser


class GitUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'avatar')
    list_filter = ('username', 'avatar')


admin.site.register(GitUser, GitUserAdmin)