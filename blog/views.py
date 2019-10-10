import math

from django.shortcuts import render

from blog.models import Post


def index(request):
    if request.GET.get('p'):
        current_page = int(request.GET.get('p'))
    else:
        current_page = 1

    pages_number = math.ceil(Post.objects.all().count() / 4)
    posts = Post.objects.all().order_by('-date')[(4 * current_page) - 4:4 * current_page]

    # TODO enforce 5 pages

    if current_page > 2:
        lower_limit = current_page - 2
    else:
        lower_limit = 1

    if current_page < pages_number - 2:
        upper_limit = current_page + 2
    else:
        upper_limit = pages_number

    nav_pages = list(range(lower_limit, upper_limit + 1))

    context = {"posts": posts, "current_page": current_page, "nav_pages": nav_pages, "pages_number": pages_number}

    return render(request, "index.html", context)


def view_post(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {"post": post}

    return render(request, "post.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
