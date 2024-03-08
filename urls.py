# myapp/urls.py
from django.urls import path
from .views import predict_list, predict_create, predict_update, predict_delete

urlpatterns = [
    path('predict/', predict_list, name='predict_list'),
    path('predict/create/', predict_create, name='predict_create'),
    path('predict/<int:pk>/update/', predict_update, name='predict_update'),
    path('predict/<int:pk>/delete/', predict_delete, name='predict_delete'),
]
