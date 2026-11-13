from django.shortcuts import get_object_or_404, render
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.filter(published=True).order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug: str):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, "blog/post_detail.html", {"post": post})


def search_posts(request):
    query = request.GET.get("q", "")
    posts = Post.objects.filter(title__icontains=query, published=True)
    return render(request, "blog/post_list.html", {"posts": posts, "query": query})


def add_comment(request, slug: str):
    post = get_object_or_404(Post, slug=slug, published=True)
    if request.method == "POST":
        author = request.POST.get("author")
        text = request.POST.get("text")
        comment = Comment.objects.create(post=post, author_name=author, text=text)
    return render(request, "blog/post_detail.html", {"post": post})
