from django.urls import path
from . import views

urlpatterns = [
    path('', views.Books.as_view(), name='books'),
    # path('uploadBook/', views.CreateBook.as_view(), name='uploadbook'),
    path('<str:id>/', views.BookDetails.as_view(), name='bookdetails'),
    path('delete/<str:id>/', views.DeleteBook.as_view(), name='deletebook'),
    path('update/<str:id>/', views.UpdateBook.as_view(), name='updatebook'),
    path('userbooks/<str:id>', views.UserBooks.as_view(), name='userbooks'),
]
