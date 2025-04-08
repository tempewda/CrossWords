from django.shortcuts import render # Import render to create HTTP responses by rendering templates
from .models import Book # Import the Book model to interact with the book data

# Create your views here.

def book_list(request):
    """
    View function to display the list of all available books.
    """
    # 1. Fetch all Book objects from the database
    #    The .objects.all() method retrieves all records from the Book table.
    books = Book.objects.all()

    # 2. Define the context dictionary to pass data to the template
    #    The keys in this dictionary ('books' in this case) will be
    #    available as variables within the template.
    context = {
        'books': books,
    }

    # 3. Render the HTML template
    #    - request: The original HttpRequest object.
    #    - 'store/book_list.html': The path to the template file we will create next.
    #    - context: The dictionary containing data for the template.
    #    This function returns an HttpResponse object containing the rendered HTML.
    return render(request, 'store/book_list.html', context)

# Add other views below as needed
