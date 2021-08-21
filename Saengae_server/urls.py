from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('pad/', PadList.as_view()),
    path('pad/<int:pk>/', PadDetail.as_view()),
    path('ingredient/', IngredientList.as_view()),
    path('ingredient/<int:pk>', IngredientDetail.as_view()),
    path('detectionInfo/', DetectionList.as_view()),
    path('review/', Review.as_view()),
    # path('detectionInfo/<int:pk>', DetectionDetail.as_view()),

]