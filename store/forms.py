from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'authors',
            'language',
            'publisher',
            'published_year',
            'status',
            'description',
            'price',
            'number_available',
            'category',  
        )
