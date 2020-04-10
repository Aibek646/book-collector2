from django.shortcuts import render
from .models import Book
# Create your views here.def

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})    