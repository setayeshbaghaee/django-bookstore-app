from django.shortcuts import render
from store.models import Category ,Book
from django.db.models import Count
from django.views.generic import ListView

def home(request):
    categories = Category.objects.annotate(num_books=Count('book'))
    best_books = Book.objects.all().order_by('-numofsells')[:8]
    new_books = Book.objects.all().order_by('-dateofadd')[:8]

    return render(request, 'core/index.html', {'categories': categories ,'best_books': best_books,'new_books': new_books})

def contact(request):
    return render(request, 'core/contact.html')

def Categoryview(request):
    categories = Category.objects.annotate(num_books=Count('book'))
    return render(request, 'core/base.html', {'categories': categories})


