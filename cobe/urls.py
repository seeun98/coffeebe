from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signup/', views.CobeAPIView.as_view(), name='signup'),
    # rest framework login
]