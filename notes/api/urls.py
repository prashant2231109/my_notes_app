from django.urls import path
from .import views

urlpatterns=[
    
    path('note/', views.notes, name="notes"),
    path('create/',views.create, name="create"),
    path('read/<str:pk>/', views.read, name="read"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),
]