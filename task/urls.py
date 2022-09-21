from django.urls import path
from . import views

urlpatterns = [
    path('', views.readTask),
    path('new/', views.createTask),
    path('update/<int:pk>', views.updateTask),
    path('delete/<int:pk>', views.deleteTask),
]