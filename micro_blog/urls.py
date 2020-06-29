from django.contrib import admin
from django.urls import path

from blog.views import BlogListView
from blog.views import BlogDetailView
from blog.views import BlogCreateView
from blog.views import BlogUpdateView

urlpatterns = [
    # path('<URL>',views(関数),ニックネーム)
    path('',BlogListView.as_view(),name="index"),
    path('<int:pk>', BlogDetailView.as_view(), name="detail"),
    path('create', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/update', BlogUpdateView.as_view(), name="update"),
    path('admin/', admin.site.urls),
]
