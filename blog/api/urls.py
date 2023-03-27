from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('blog-view/<str:pk>/', views.blogView, name="blogview"),
    path('add-blog/', views.blogAdd, name="blogadd"),
    path('update-blog/<str:pk>/', views.blogUpdate, name="blogupdate"),
]