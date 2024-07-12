from django.urls import path
from . import views, admin

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("about", views.contact_us, name="contact"),
    path("categories", views.categories, name="categories"),
    path("search_results", views.search_results, name="search-results"),
    path("add_book", views.add_book_view, name="add-book"),
    path('delete_book/<book_id>', views.delete_book, name="delete-book"),
    path('update_book/<book_id>', views.update_book, name="update-book"),
    path("add_category",views.add_category, name="add-category"),
    path('delete_category/<category_id>', views.delete_category, name="delete-category"),
    path('update_category/<category_id>', views.update_category, name="update-category")
]

