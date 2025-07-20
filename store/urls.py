from django.urls import path
from . import  views

urlpatterns = [
    path('', views.combined_view, name='book'),
    path('<int:pk>/', views.catandbookview, name='book_detail'),
    path('category/<int:pk>/', views.category_getbook, name='category_detail'),
    path('lastes/', views.lastes_sort, name='Latest'),
    path('popularity/', views.lastes_sort, name='Popularity'),

    path('empbook/', views.BookListView.as_view(), name='empbook'),

    path('add/', views.BookCreateView.as_view(), name='add_book'),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='update_book'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='delete_book'),

    path('empauthor/', views.AuthorListView.as_view(), name='empauthor'),

    path('add/author', views.AuthorCreateView.as_view(), name='add_author'),
    path('update/author/<int:pk>/', views.AuthorUpdateView.as_view(), name='update_author'),
    path('delete/author/<int:pk>/', views.AuthorDeleteView.as_view(), name='delete_author'),


]


