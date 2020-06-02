from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView, CreateView

from articles.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = 'articles'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/detail.html'
    context_object_name = 'article'

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'articles/update.html'
    context_object_name = 'article'


class ArticleDeleteView(DeleteView): # new
    model = Article
    template_name = 'articles/delete.html'
    success_url = reverse_lazy('article-list')


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'body', 'author']
    context_object_name = 'article'
    template_name = 'articles/create.html'


