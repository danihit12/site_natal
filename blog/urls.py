from django.urls import path
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostEditView, PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_update'),   # <-- AQUI!!!
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
