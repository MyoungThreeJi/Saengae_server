from rest_framework import generics

from .models import Pad, Ingredient, Detection, Review
from .serializers import PadSerializer, IngredientSerializer, DetectionSerializer, ReviewSerializer


# Create your views here.
class PadList(generics.ListCreateAPIView):
    queryset = Pad.objects.all()
    serializer_class = PadSerializer


class PadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pad.objects.all()
    serializer_class = PadSerializer


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class DetectionList(generics.ListCreateAPIView):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer


class DetectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Detection.objects.all()
    serializer_class = DetectionSerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

