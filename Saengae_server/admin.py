from django.contrib import admin
from django.utils.html import format_html

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
    # readonly_fields = ['id', 'name', 'enName', 'average', 'max', 'min', 'sideEffect']


class PadAdmin(admin.ModelAdmin):
    inlines = (DetectionInline, ReviewInline,)
    list_display = ['id', 'image_tag', 'manufacturer', 'name']
    # readonly_fields = ['id', 'manufacturer', 'name']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50px;"/>'.format(obj.image))
    image_tag.short_description = 'Image'


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'pad', 'created', 'updated']
    # readonly_fields = ['pad', 'star1', 'star2', 'star3', 'star4', 'content', 'created', 'updated']


admin.site.register(Pad, PadAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Review, ReviewAdmin)


