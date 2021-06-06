from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article

class ArticleCreateView(LoginRequiredMixin, CreateView):
    """View for posting a new article."""
    model = Article
    fields = ('title', 'body')
    template_name = 'article_new.html' 

    def form_valid(self, form):
        """Automatically sets current user as author."""
        form.instance.author = self.request.user
        return super().form_valid(form)       

class ArticleListView(LoginRequiredMixin, ListView):
    """View for displaying newspaper articles."""
    model = Article
    template_name = 'article_list.html' 

class ArticleDetailView(LoginRequiredMixin, DetailView):
       """View for detail view of an article."""
       model = Article
       template_name = 'article_detail.html' 

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View for editing an article."""
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

    def test_func(self):
        """Checks if current user matches the article author."""
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View for deleting an article."""
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')  

    def test_func(self):
        """Checks if current user matches the article author."""
        obj = self.get_object()
        return obj.author == self.request.user