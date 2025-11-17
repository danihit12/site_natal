from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/novo/', views.post_create, name='post_create'),
    path('post/<int:pk>/editar/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/deletar/', views.post_delete, name='post_delete'),
]