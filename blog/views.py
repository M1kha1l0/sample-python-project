from django.shortcuts import get_object_or_404, render

from .models import Post


def post_list(request):
    posts = Post.objects.filter(published=True).order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, slug: str):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, "blog/post_detail.html", {"post": post})



def add_reaction(request, slug: str):
    post = get_object_or_404(Post, slug=slug, published=True)
    if request.method == "POST":
        reaction_type = request.POST.get("type", "like")
        Reaction.objects.create(post=post, reaction_type=reaction_type)
        return render(request, "blog/post_detail.html", {"post": post})
    return render(request, "blog/post_detail.html", {"post": post})
