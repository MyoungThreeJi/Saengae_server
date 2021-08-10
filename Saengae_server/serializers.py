from .models import Pad
from rest_framework import serializers


# class IngredientInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ingredient_info
#         fields = ['igd_koName', 'igd_enName', 'ing_detection', 'igd_sideEffect']


class PadSerializer(serializers.ModelSerializer):
    # Ingredients = IngredientInfoSerializer(many=True, read_only=True)

    class Meta:
        model = Pad
        fields = '__all__'
