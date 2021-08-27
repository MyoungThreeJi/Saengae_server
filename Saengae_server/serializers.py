from .models import Pad, Ingredient, Detection, Review
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'enName', 'average', 'max', 'min', 'sideEffect')


class DetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detection
        fields = ('pad', 'ingredient', 'detection')


class ReviewSerializer(serializers.ModelSerializer):
    # review_create = serializers.
    class Meta:
        model = Review
        fields = ('userName', 'userImage', 'pad', 'star1', 'star2', 'star3', 'star4', 'content', 'created', 'updated')


class PadSerializer(serializers.ModelSerializer):
    queryset_igd = Detection.objects.all()
    ingredients = IngredientSerializer(queryset_igd, many=True, required=False) #read_only=True

    class Meta:
        model = Pad
        fields = ('id', 'name', 'manufacturer', 'image', 'ingredients', 'rank', 'safeScore')
