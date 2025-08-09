from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm, ExampleForm  # Import ExampleForm here

def example_form_view(request):
    """
    View to display and process ExampleForm securely.

    - Handles both GET and POST requests.
    - On GET: renders empty form.
    - On POST: validates form input safely.
    - If valid, processes and returns a message.
    """
    if request.method == 'POST':
        # Bind form with POST data
        form = ExampleForm(request.POST)
        
        # Validate form inputs (clean and safe)
        if form.is_valid():
            # Retrieve cleaned data from form
            example_value = form.cleaned_data['example_field']
            
            # Render template with form and success message
            return render(request, 'bookshelf/form_example.html', {
                'form': form,
                'message': f'You entered: {example_value}'
            })
    else:
        # If GET request, create a new unbound form
        form = ExampleForm()
    
    # Render the form template for both GET and invalid POST cases
    return render(request, 'bookshelf/form_example.html', {'form': form})
