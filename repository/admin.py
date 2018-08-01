from django.contrib import admin

from repository.models import Repository


class RepositoryAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'description', 'url', 'language', 'watchers_count')
    list_filter = ('owner', 'name', 'description', 'url', 'language', 'watchers_count')
    search_fields = ('owner', 'name')


admin.site.register(Repository, RepositoryAdmin)