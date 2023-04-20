from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
        
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def detail(request, post_pk: int):
    post = Post.objects.get(pk=post_pk)
    
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)

@login_required
def answer(request, post_pk, answer):
    post = Post.objects.get(pk=post_pk)

    if request.user not in post.select1_user.all() and request.user not in post.select2_user.all():
        if answer == post.select1_content:
            post.select1_user.add(request.user)
        elif answer == post.select2_content:
            post.select2_user.add(request.user)
    
    return redirect('posts:detail', post_pk)