from django.urls import path
from . import views

urlpatterns = [
    path('index',views.Index.as_view()),
    path('order',views.Order.as_view()),
]
