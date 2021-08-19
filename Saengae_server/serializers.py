from .models import Pad, Ingredient, Detection
from rest_framework import serializers


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'enName', 'sideEffect')


class DetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detection
        fields = ('pad_id', 'ingredient_id', 'detection')


class PadSerializer(serializers.ModelSerializer):
    queryset = Detection.objects.all()
    ingredients = IngredientSerializer(queryset, many=True, read_only=True)

    class Meta:
        model = Pad
        fields = ('id', 'name', 'manufacturer', 'image', 'ingredients')
