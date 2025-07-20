from django.db import models

class Author(models.Model):
    Authorname = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.Authorname

class Category(models.Model):
    Categoryname = models.CharField(max_length=100)

    def __str__(self):
        return self.Categoryname
    
class Publisher(models.Model):
    Publishername = models.CharField(max_length=100)
    website = models.URLField(blank=True) 
    email = models.EmailField(blank=True) 

    def __str__(self):
        return self.Publishername


class Book(models.Model):
    STATUS_CHOICES=(
        ("A", "Available"),
        ("N","NonExistent")
    )

    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    language = models.CharField(max_length= 100)
    publisher = models.ForeignKey(Publisher , on_delete=models.CASCADE)
    published_year = models.IntegerField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="A")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    number_available = models.IntegerField()
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)

    numofsells = models.PositiveIntegerField(default=0)
    dateofadd=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title