from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    context = {
        'hi': 'hello world',
    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)