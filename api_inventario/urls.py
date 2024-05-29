from django.urls import path
from .views import *
from .views import index

urlpatterns=[
    path('api/inventario',Inventario_APIView.as_view()),
    path('index/',index),

]