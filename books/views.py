from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from books.models import Book, Comment


class BookListView(ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'

# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'

def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comments = book.comments.all()
    return render(request, 'books/book_detail.html', {'book': book, 'comments': book_comments})


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'cover', ]
    template_name = 'books/book_create.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price']
    template_name = 'books/book_update.html'


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')