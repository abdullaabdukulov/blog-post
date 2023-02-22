from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blog_single/', views.blog_single),
]