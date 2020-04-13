from django.shortcuts import render, redirect
from .models import Book, Translator
from .forms import NewPrint

# Create your views here.def

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')    

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})    


def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    trans_book_no_have = Translator.objects.exclude(id__in = book.translators.all().values_list('id'))
    print_form = NewPrint()
    return render(request, 'books/book_detail.html', {'book': book, 'print_form': print_form, 'trans': trans_book_no_have})    


def add_print(request, book_id):
    form = NewPrint(request.POST)
    if form.is_valid():
        new_print = form.save(commit=False)
        new_print.book_id = book_id
        new_print.save()
    return redirect('detail', book_id=book_id)        