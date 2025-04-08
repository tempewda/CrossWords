# store/models.py
from django.db import models

class Book(models.Model):
    """
    Represents a book in the bookstore.
    Each attribute corresponds to a column in the database table.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True, help_text='13 Character ISBN')
    description = models.TextField(blank=True) # Allows longer text, can be empty
    price = models.DecimalField(max_digits=10, decimal_places=2) # Suitable for currency
    stock_quantity = models.PositiveIntegerField(default=0) # Ensures non-negative integer
    # For simplicity, using a URL field for the cover image.
    # Could be replaced with ImageField for actual uploads later.
    cover_image_url = models.URLField(max_length=2000, blank=True, null=True) # Stores a web address for the image
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set timestamp when a book record is first created
    updated_at = models.DateTimeField(auto_now=True)     # Automatically set timestamp every time a book record is saved

    def __str__(self):
        """
        Returns a string representation of the Book object,
        useful in the admin interface and debugging.
        """
        return f"{self.title} by {self.author}"

    class Meta:
        # Optional: Defines metadata for the model
        ordering = ['title'] # Default sorting order when fetching multiple books
