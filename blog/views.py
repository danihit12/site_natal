from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, CommentForm


# LISTAGEM DE POSTS
def post_list(request):
    posts = Post.objects.all()
    neve = range(40)   # 40 flocos de neve
    return render(request, 'blog/post_list.html', {'posts': posts, 'neve': neve})

# DETALHE DO POST + FORM DE COMENTÁRIOS
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'form': form,
    })


# CRIAR POST
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})


# EDITAR POST
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {'form': form})


# DELETAR POST
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':  # opcional, mas recomendado
        post.delete()
        return redirect('post_list')

    # página de confirmação de remoção
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
