from rest_framework import generics

from .models import Pad, Ingredient_info
from .serializers import PadSerializer, IngredientInfoSerializer


# Create your views here.
class PadList(generics.ListCreateAPIView):
    queryset = Pad.objects.all()
    serializer_class = PadSerializer


class PadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pad.objects.all()
    serializer_class = PadSerializer
