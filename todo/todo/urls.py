from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [

    path('', views.home_view, name='home'),
    path('add_todo/', views.add_todo, name='add'),
    path('update_todo/<int:pk>/', views.update_todo, name='update'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete'),

    path('admin/', admin.site.urls),
]
