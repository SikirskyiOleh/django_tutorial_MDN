from django.shortcuts import render

from .models import Author, Book, BookInstance, Genre, Language


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available book (status = 'a)
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default
    num_authors = Author.objects.count()

    # Number of genres that contain a particular word (case insensitive)
    num_spec_genres = Genre.objects.filter(name__icontains='Fantacy').count()

    # Number of books that contain a particular word (case insensitive)
    num_spec_books = Book.objects.filter(title__icontains='The').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instance_available': num_instances_available,
        'num_authors': num_authors,
        'num_spec_genres': num_spec_genres,
        'num_spec_books': num_spec_books,
    }

    # Render the HTML template index.html with the date in the context variable
    return render(request, 'index.html', context=context)
