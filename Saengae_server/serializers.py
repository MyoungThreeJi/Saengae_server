from django.db.models import Avg

from .models import Pad, Ingredient, Detection, Review, Map
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'enName', 'average', 'max', 'min', 'sideEffect')


class DetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detection
        fields = ('pad', 'ingredient', 'detection', 'ingredient_info')


class ReviewSerializer(serializers.ModelSerializer):
    # review_create = serializers.
    class Meta:
        model = Review
        fields = ('userName', 'userImage', 'pad', 'star1', 'star2', 'star3', 'star4', 'content', 'created', 'updated')


class PadSerializer(serializers.ModelSerializer):
    queryset_igd = Detection.objects.all()
    ingredients = IngredientSerializer(queryset_igd, many=True, required=False) #read_only=True
    # ingredients.objects.aggregate(safeScore=Avg('성분별 점수'))

    class Meta:
        model = Pad
        fields = ('id', 'name', 'manufacturer', 'image', 'ingredients', 'rank', 'safeScore')


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('name', 'type', 'address', 'longitude', 'latitude', 'Phone')
