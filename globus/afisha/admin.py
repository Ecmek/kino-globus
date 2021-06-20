from django.contrib import admin

from .models import Cinema, ShowTime

class CinemaAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'trailer', 'description', 'mpaa',)
    search_fields = ('title')
    list_filter = ('show_date')
    empty_value_display = '-пусто-'

class ShowTimeAdmin(admin.ModelAdmin):
    list_display = ('datetime', 'price', 'format')

admin.site.register(Cinema, CinemaAdmin)
admin.site.register(ShowTime, ShowTimeAdmin)