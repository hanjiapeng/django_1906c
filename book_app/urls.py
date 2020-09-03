from django.urls import path
from book_app import views

urlpatterns = [
    path('login/', views.login),
]
