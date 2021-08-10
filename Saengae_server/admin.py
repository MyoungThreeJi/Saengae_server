from django.contrib import admin
from .models import Pad


# Register your models here.
class PadAdmin(admin.ModelAdmin):
    list_display = ['id', 'manufacturer', 'name', 'image']


admin.site.register(Pad, PadAdmin)
# admin.site.register(Ingredient_info)
