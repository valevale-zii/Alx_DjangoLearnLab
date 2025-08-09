from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm, ExampleForm  # Import ExampleForm here

def example_form_view(request):
    """
    View to display and process ExampleForm securely.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process form.cleaned_data here
            example_value = form.cleaned_data['example_field']
            return render(request, 'bookshelf/form_example.html', {'form': form, 'message': f'You entered: {example_value}'})
    else:
        form = ExampleForm()
    
    return render(request, 'bookshelf/form_example.html', {'form': form})
