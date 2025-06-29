

from django.urls import path
from . import views

app_name="bookstore"
urlpatterns = [
    path("", views.index, name="home-index")

    ,path("book_store_list", views.show_books_list, name="book_store-index")
    ,path("book_store_details/<int:book_id>", views.book_details, name="details-index")
    ,path("book-delete/<int:book_id>", views.delete_book, name="delete-index"),
    path("book-update/<int:book_id>", views.update_book, name="update-index"),  
    path("book-add", views.add_book, name="add-index"),  

]
