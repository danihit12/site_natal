from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

# LISTAGEM
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

# DETALHE
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# CRIAR POST (SEM FORM)
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')

        Post.objects.create(
            title=title,
            content=content,
            image=image
        )
        return redirect('post_list')

    return render(request, 'blog/post_create_manual.html')

# EDITAR POST (SEM FORM)
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')

        if request.FILES.get('image'):
            post.image = request.FILES.get('image')

        post.save()
        return redirect('post_detail', pk=post.pk)

    return render(request, 'blog/post_edit_manual.html', {'post': post})

# DELETAR POST (COM CONFIRMAÇÃO)
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'blog/post_delete_confirm.html', {'post': post})
