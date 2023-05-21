from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Book

# Create your views here.


class BookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"
    permission_required = "books.special_status"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = "books.special_status"


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    # queryset = Book.objects.filter(title__icontains="API")

    def get_queryset(self):
        search = self.request.GET.get("q")
        return self.model.objects.filter(
            Q(title__contains=search) | Q(title__icontains=search)
        )
