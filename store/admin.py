# store/admin.py
from django.contrib import admin
from .models import Book # Import the Book model from models.py

# This decorator is a common way to register and customize admin options
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Book model.
    Allows customization of how books are displayed and managed in the admin interface.
    """
    # Defines which fields are displayed in the list view of books
    list_display = ('title', 'author', 'price', 'stock_quantity', 'isbn')
    # Adds a search box to search by these fields
    search_fields = ('title', 'author', 'isbn')
    # Adds filters to the right sidebar based on these fields
    list_filter = ('author',)
    # Sets the default sorting order in the admin list view
    ordering = ('title',)

# Alternatively, for basic registration without customization, you could just use:
# admin.site.register(Book)

