from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.postListView.as_view(), name="post"),
    url(r'tags', views.tagListView.as_view(),name="tag"),
    url(r'categories', views.CategoryView.as_view(), name='category')
]