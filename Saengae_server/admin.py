from django.contrib import admin
from .models import Pad, Ingredient, Detection


# Register your models here.
class DetectionInline(admin.TabularInline):
    model = Detection
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    inlines = (DetectionInline,)
    list_display = ['id', 'name', 'enName']
    readonly_fields = ['id', 'name', 'enName', 'average', 'max', 'min', 'sideEffect']


class PadAdmin(admin.ModelAdmin):
    inlines = (DetectionInline,)
    list_display = ['id', 'manufacturer', 'name']
    readonly_fields = ['id', 'manufacturer', 'name', 'image']


admin.site.register(Pad, PadAdmin)
admin.site.register(Ingredient, IngredientAdmin)


