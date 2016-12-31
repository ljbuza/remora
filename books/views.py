from django.shortcuts import render
from books.models import Book


def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            errors.append('Enter a search term')
            # return render(request, 'search_form.html', {'error': error})
        elif len(query) > 20:
            errors.append('Please limit query to 20 characters')
        else:
            return render(request, 'search_form.html',
                {'submitted': True, 'results': Book.objects.filter(title__icontains=query)})
    return render(request, 'search_form.html', {'errors': errors})
