from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from books.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price']
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('book_list')
