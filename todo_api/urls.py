from django.urls import path
from . import views
urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('index/',views.index, name="index"),
    path('create/', views.create, name="create"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<str:pk>/', views.delete, name="delete"),
    path('yes_finish/<str:pk>/', views.yes_finish, name="yes_finish"),
    path('no_finish/<str:pk>/', views.no_finish, name="no_finish"),
  ]