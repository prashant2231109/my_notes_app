from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name="create"),
    path('delete_view/<int:id>/', views.delete_view, name='delete_view'),
    path('edit_view/<int:id>/', views.edit_view, name='edit_view'),
  
    

]
