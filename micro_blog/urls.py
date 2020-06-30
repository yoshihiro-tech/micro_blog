from django.contrib import admin
from django.urls import path

from blog.views import BlogListView
from blog.views import BlogDetailView
from blog.views import BlogCreateView
from blog.views import BlogUpdateView
from blog.views import BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name="index"),
    path('<int:pk>', BlogDetailView.as_view(), name="detail"),
    path('create', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/update', BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name="delete"),
    path('admin/', admin.site.urls),
]
