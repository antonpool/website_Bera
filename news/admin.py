from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin



admin.site.register(
    models.Category,
    MPTTModelAdmin,
    list_display=('name',),
    prepopulated_fields = {'slug' : ('name',) }
)

@admin.register(models.Articles)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'anons', 'date'] # строки в админ панели
    prepopulated_fields = {'slug' : ('title', 'anons') } #автозаполнение поле slug
