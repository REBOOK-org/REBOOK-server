from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name='books'),
    path('uploadBook/', views.CreateBook.as_view(), name='create_books'),
]
