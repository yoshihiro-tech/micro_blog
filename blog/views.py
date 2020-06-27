from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView

from .models import Blog


class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

