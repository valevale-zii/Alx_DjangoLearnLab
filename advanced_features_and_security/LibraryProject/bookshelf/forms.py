from django import forms

from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True)

class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=100, required=True)
