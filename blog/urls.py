from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.postListView.as_view(), name="post"),
    url(r'(?P<pk>\d+)/', views.postRetrieveView.as_view(), name="postDetail"),
    url(r'tags', views.tagListView.as_view(),name="tag"),
    url(r'categories', views.CategoryView.as_view(), name='category')
]