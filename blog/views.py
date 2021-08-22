from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'  # шаблон, по умолчанию news/news_list.html для ListView
    context_object_name = 'posts'  # Объект в шаблоне, по умолчанию object_list для ListView
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


def index(request):
    return render(request, 'blog/index.html')


def get_category(request, slug):
    return render(request, 'blog/category.html')


def get_post(request, slug):
    return render(request, 'blog/category.html')