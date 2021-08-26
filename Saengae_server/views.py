import random

from rest_framework import generics

from .models import Pad, Ingredient, Detection, Review
from .serializers import PadSerializer, IngredientSerializer, DetectionSerializer, ReviewSerializer


def randomUser():
    first = random.choice(['이상한', '매콤한', '행복한', '구수한', '귀여운', '섭섭한', '시원한', '어마무시한', '찰진', '혼란스러운'])
    last = random.choice(['메뚜기', '앨리스', '낚지볶음', '피카츄', '오무라이스', '병아리', '만두', '가락국수', '순대국', '애벌레'])
    username = first + " " + last
    return username


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


class ReviewCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(userName=randomUser()) # self.request.user


class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

