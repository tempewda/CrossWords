# store/urls.py

from django.urls import path
from . import views  # Import views from the current app directory

# Define an app namespace for easier URL referencing in templates (optional but good practice)
app_name = 'store'

urlpatterns = [
    # Map the 'root' path of the app ('') to the book_list view
    # When included in the project urls, if the prefix is '', this will match the site homepage.
    # We give it a name 'book-list' which can be used to refer to this URL pattern elsewhere.
    path('', views.book_list, name='book-list'),

    # Add other store-specific URL patterns here later (e.g., for book details)
    # path('book/<int:book_id>/', views.book_detail, name='book-detail'),
]
