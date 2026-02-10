from django.shortcuts import get_object_or_404, render

from .models import Post, Tag


def post_list(request):
    posts = Post.objects.filter(published=True).order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug: str):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, "blog/post_detail.html", {"post": post})


def tag_detail(request, slug: str):
    tag = get_object_or_404(Tag, slug=slug)
    posts = tag.posts.filter(published=True).order_by("-created_at")
    return render(
        request,
        "blog/post_list.html",
        {
            "posts": posts,
            "current_tag": tag,
        },
    )

