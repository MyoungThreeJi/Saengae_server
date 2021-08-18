from rest_framework import generics

from .models import Pad, Ingredient
from .serializers import PadSerializer, IngredientSerializer


# Create your views here.
class PadList(generics.ListCreateAPIView):
    queryset = Pad.objects.all()
    serializer_class = PadSerializer


class PadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pad.objects.all()
    serializer_class = PadSerializer


# class IngredientDetailList(generics.ListCreateAPIView):
#
# class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):


# from rest_framework.viewsets import ModelViewSet
#
# from Saengae_server.models import Pad, Detection, Ingredient
# from Saengae_server.serializers import PadSerializer, DetectionSerializer, IngredientSerializer
#
#
# class PadList(ModelViewSet):
#     queryset = Pad.objects.all()
#     serializer_class = PadSerializer
#
#
# class DetectionViewSet(ModelViewSet):
#     queryset = Detection.objects.all()
#     serializer_class = DetectionSerializer
#
#
# class IngredientViewSet(ModelViewSet):
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer
