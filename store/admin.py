from django.contrib import admin
from .models import Author, Category, Book, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 
        'price', 
        'number_available', 
        'status', 
        'display_authors', 
        'display_publishers', 
        'display_categories'
    )
    search_fields = ('title', 'authors__Authorname', 'publisher__Publishername', 'category__Categoryname')
    list_filter = ('status', 'language','category__Categoryname' ,'publisher__Publishername' , 'authors__Authorname' )
    list_editable = ['status', 'price' , 'number_available']
    sortable_by = ['title']

    def display_authors(self, obj):
        return ", ".join(author.Authorname for author in obj.authors.all())
    display_authors.short_description = 'Authors'

    def display_publishers(self, obj):
        return ", ".join(pub.Publishername for pub in obj.publisher.all())
    display_publishers.short_description = 'Publishers'

    def display_categories(self, obj):
        return ", ".join(cat.Categoryname for cat in obj.category.all())
    display_categories.short_description = 'Categories'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('Authorname',)
    search_fields = ('Authorname',)
    sortable_by = ['Authorname']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Categoryname',)
    search_fields = ('Categoryname',)
    sortable_by = ['Categoryname']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('Publishername',)
    search_fields = ('Publishername',)
    sortable_by = ['Publishername']
