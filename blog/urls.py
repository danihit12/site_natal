from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostEditView, PostDeleteView,
    CategoryListView, category_detail
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path("categorias/", CategoryListView.as_view(), name="category_list"),
    path('categoria/<int:category_id>/', category_detail, name='category_detail'),
]
