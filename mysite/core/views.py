from django.shortcuts import render
from django.utils import timezone
from blog.models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib import messages
from django.http import JsonResponse

# Import Pagination Stuff
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def base(request):
    return render(request, 'core/base.html')

def frontpage(request):
    posts = Post.objects.latest('published_date')
    return render(request, 'core/frontpage.html', {'posts': posts})

def blog(request):
    posts = Post.objects.all()
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'core/blog.html', {'posts': posts})

def post_list(request):
    queryset_list = Post.objects.all().order_by('-published_date')
    query = request.GET.get('page')
    if query:
        queryset_list = queryset_list.filter(title__icontains=query)
    paginator = Paginator(queryset_list, 3) # Show 3 per page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'core/post_list.html', {'posts': posts})

def post_detail(request, slug):
    posts = Post.objects.get(slug=slug)
    #posts = get_object_or_404(Post, pk=pk)
    return render(request, 'core/post_detail.html', {'posts': posts})

def post_new(request, slug):
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, "Post successful")
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
        messages.error(request, "Failed :(")
    return render(request, 'core/post_edit.html', {'form': form})


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, "Saved")
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'core/post_edit.html', {'form': form})

from django.shortcuts import redirect

def add_comment_to_post(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = posts
            comment.save()
            return redirect('post_detail', slug=posts.slug)  # Redirect to post_detail with the updated comment
    else:
        form = CommentForm()
    return render(request, 'core/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.slug)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.slug)

def about(request):
    return render(request, 'core/about.html')

def coming_soon_page(request):
    return render(request, 'core/coming_soon_page.html')