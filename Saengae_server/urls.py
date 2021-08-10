from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('pad/', PadList.as_view()),
    path('pad/<int:pk>/', PadDetail.as_view())
]