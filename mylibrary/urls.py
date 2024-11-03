from django.urls import path, re_path
from django.contrib import admin

from bookshelf import views
from bookshelf import old_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
    path('my-books/', views.BooksView.as_view(), name='my_books'),
    path('book-detail-by-id/<str:pk>/', views.BookDetailByIdView.as_view(), name='book_detail_by_id'),
    path('book-detail-by-code/<str:code>/', views.BookDetailByCodeView.as_view(), name='book_detail_by_code'),
    path('book-update/<str:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('book-create/', views.BookCreateView.as_view(), name='book_create'), 
    path('author-create/', views.AuthorCreateView.as_view(), name='author_create'),   

    # Old views
    path('old/welcome/', old_views.welcome, name='old_welcome'),
    path('old/my-books/', old_views.get_books_list, name='old_my_books'),
    path('old/book-detail-by-id/<str:pk>/', old_views.get_book_by_id, name='old_book_detail_by_id'),
    path('old/book-detail-by-code/<str:code>/', old_views.get_book_by_code, name='old_book_detail_by_code'),
    path('old/book-update/<str:pk>/', old_views.edit_book, name='old_book_update'),
]
