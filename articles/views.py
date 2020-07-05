from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article

# Create your views here.


class ArticleViewMixin(LoginRequiredMixin):
    model = Article
    login_url = 'login'


class ArticleListView(ArticleViewMixin, ListView):
    template_name = 'articles/index.html'


class ArticleDetailView(ArticleViewMixin, DetailView):
    template_name = 'articles/detail.html'


class ArticleCreateView(ArticleViewMixin, CreateView):
    fields = ('title', 'body',)
    template_name = 'articles/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(ArticleViewMixin, UserPassesTestMixin, UpdateView):
    fields = ('title', 'body', )
    template_name = 'articles/update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(ArticleViewMixin, UserPassesTestMixin, DeleteView):
    template_name = 'articles/delete.html'
    success_url = reverse_lazy('article:index')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
