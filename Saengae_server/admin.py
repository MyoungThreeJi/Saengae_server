from django.contrib import admin
from .models import Pad, Ingredient, Detection, Review


# Register your models here.
class DetectionInline(admin.TabularInline):
    model = Detection
    extra = 1


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class IngredientAdmin(admin.ModelAdmin):
    inlines = (DetectionInline,)
    list_display = ['id', 'name', 'enName']
    readonly_fields = ['id', 'name', 'enName', 'average', 'max', 'min', 'sideEffect']


class PadAdmin(admin.ModelAdmin):
    inlines = (DetectionInline, ReviewInline,)
    list_display = ['id', 'manufacturer', 'name']
    readonly_fields = ['id', 'manufacturer', 'name', 'image']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'pad', 'created', 'updated']
    readonly_fields = ['pad', 'star1', 'star2', 'star3', 'star4', 'content', 'created', 'updated']


admin.site.register(Pad, PadAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Review, ReviewAdmin)


