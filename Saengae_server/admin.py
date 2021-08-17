from django.contrib import admin
from .models import Pad, Ingredient, Detection


# Register your models here.
class DetectionInline(admin.TabularInline):
    model = Detection
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    inlines = (DetectionInline,)
    # list_display = ['id', 'manufacturer', 'name', 'image']


class PadAdmin(admin.ModelAdmin):
    inlines = (DetectionInline,)
    # list_display = ['id', 'manufacturer', 'name', 'image']


admin.site.register(Pad, PadAdmin)
admin.site.register(Ingredient, IngredientAdmin)


