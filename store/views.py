from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import BookForm
from django.views.generic import ListView, DetailView,CreateView , UpdateView , DeleteView
from . models import Book,Category,Author
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import PermissionRequiredMixin
# @login_required
# def add_book(request):
#     if request.user.groups.filter(name='employee').exists():
#         if request.method == 'POST':
#             form = BookForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('book_list')
#         else:
#             form = BookForm()
#         return render(request, 'book/add_book.html',{'form': form})
#     else:
#         return render(request, 'book/not_authorized.html')


def home(request):
    categories = Category.objects.all()
    return render(request, 'core/index.html', {'categories': categories})


class BookListView(ListView):
    model=Book
    template_name = 'store/allbook.html'
    paginate_by = 10


class CategoryListView(ListView):
    model=Category
    template_name = 'core/index.html'



class BookDetailView(DetailView):
    model = Book


def combined_view(request):
    categories = Category.objects.all()  
    price_filters = request.GET.getlist('price')
    availability_filters = request.GET.getlist('availability')

    books = Book.objects.all()

    if price_filters:
        q_objects = Q()
        for price_range in price_filters:
            if '-' in price_range:
                try:
                    min_price, max_price = map(int, price_range.split('-'))
                    q_objects |= Q(price__gte=min_price, price__lt=max_price)
                except ValueError:
                    continue  
        books = books.filter(q_objects)

    if availability_filters:
        if "in" in availability_filters and "out" not in availability_filters:
            books = books.filter(status='A')
        elif "out" in availability_filters and "in" not in availability_filters:
            books = books.filter(status='N')

    paginator = Paginator(books, 9) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'store/allbook.html', {'books': books, 'categories': categories , 'page_obj': page_obj})


def category_getbook(request, pk):
    category = Category.objects.get(id=pk)      
    books = Book.objects.filter(category=category).only('title', 'price').prefetch_related('category')
    
    return render(request, 'store/category_detail.html', {'books': books, 'category': category})


def catandbookview(request,pk):
    book = get_object_or_404(Book, id=pk)
    categories = book.category.all()
    categories_book = Book.objects.filter(category__in=categories).exclude(id=book.id).distinct()
    categories = Category.objects.all()


    return render(request, 'store/book_detail.html', {'book': book, 'categories_book': categories_book , 'categories':categories })



def lastes_sort(request):
    categories = Category.objects.all()      

    new_books = Book.objects.all().order_by('-dateofadd')
    return render(request, 'store/allbook.html', {'categories': categories ,'books': new_books})

def popularity(request):
    categories = Category.objects.all()      
    books = Book.objects.all().order_by('-numofsells')
    return render(request, 'store/allbook.html', {'categories': categories ,'books': books})





#employee_views
class BookListView(PermissionRequiredMixin,ListView):
    model=Book
    permission_required = 'store.view_book'
    template_name = 'store/empbook.html'



class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'language','authors','published_year','publisher', 'description','price','number_available','category','image']
    permission_required = 'store.add_book'
    template_name = 'store/add_book.html'
    success_url = reverse_lazy('empbook') 


class BookUpdateView(PermissionRequiredMixin,UpdateView):
    model = Book
    permission_required = 'store.change_book'
    fields = ['title', 'language','authors','published_year','publisher', 'description','price','number_available','category','image']
    template_name = 'store/update_book.html' 
    success_url = reverse_lazy('empbook') 


class BookDeleteView(PermissionRequiredMixin,DeleteView):
    model = Book
    permission_required = 'store.delete_book'
    template_name = 'store/empbook.html' 
    success_url = reverse_lazy('empbook') 




#Authers 
class AuthorListView(PermissionRequiredMixin,ListView):
    model=Author
    permission_required = 'store.view_Author'
    template_name = 'store/empAuthor.html'



class AuthorCreateView(PermissionRequiredMixin, CreateView):
    model = Author
    fields = ['Authorname', 'bio','birth_date']
    permission_required = 'store.add_Author'
    template_name = 'store/add_Author.html'
    success_url = reverse_lazy('empauthor') 


class AuthorUpdateView(PermissionRequiredMixin,UpdateView):
    model = Author
    permission_required = 'store.change_Author'
    fields = ['Authorname', 'bio','birth_date']
    template_name = 'store/update_Author.html' 
    success_url = reverse_lazy('empauthor') 


class AuthorDeleteView(PermissionRequiredMixin,DeleteView):
    model = Author
    permission_required = 'store.delete_Author'
    template_name = 'store/empAuthor.html' 
    success_url = reverse_lazy('empauthor') 