
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .models import Blog

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ["content"]
    success_url = reverse_lazy("index")

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["content"]

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy("detail", kwargs={"pk": blog_pk})
        return url
