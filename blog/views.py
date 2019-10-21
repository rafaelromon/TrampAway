import math

from django.contrib import messages
from django.shortcuts import render
from django.utils.translation import gettext as _

from blog.forms import MessageForm
from blog.models import Post, Author, Comment


def index(request):
    posts = Post.objects.all()

    if request.GET.get('p'):
        current_page = int(request.GET.get('p'))
    else:
        current_page = 1

    pages_number = math.ceil(posts.count() / 4)
    posts = posts.order_by('-date')[(4 * current_page) - 4:4 * current_page]

    if current_page > 2:
        lower_limit = current_page - 2
    else:
        lower_limit = 1

    if current_page < pages_number - 2:
        upper_limit = current_page + 2
    else:
        upper_limit = pages_number

    nav_pages = list(range(lower_limit, upper_limit + 1))
    founder = Author.objects.get(founder=True)
    featured_posts = Post.objects.all().filter(featured=True)

    context = {"posts": posts, "current_page": current_page, "nav_pages": nav_pages, "pages_number": pages_number,
               "founder": founder, "featured_posts": featured_posts}

    return render(request, "index.html", context)


def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    featured_posts = Post.objects.all().filter(featured=True)

    context = {"post": post, "featured_posts": featured_posts}

    return render(request, "post.html", context)


def about(request):
    authors = Author.objects.all()

    context = {"authors": authors}

    return render(request, "about.html", context)


def contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        form = MessageForm(request.POST)

        if form.is_valid():

            comment = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "message": form.cleaned_data["message"]
            }

            Comment.objects.create(**comment)

            messages.add_message(request, messages.SUCCESS, _('Thank you for contacting us'))

        else:
            messages.add_message(request, messages.ERROR, _('Form not valid.'))

    else:
        form = MessageForm()

    context = {"form": form}

    return render(request, "contact.html", context)


def view_author(request, username):
    author = Author.objects.get(user__username=username)
    posts = Post.objects.filter(author=author)

    if request.GET.get('p'):
        current_page = int(request.GET.get('p'))
    else:
        current_page = 1

    pages_number = math.ceil(posts.count() / 4)
    posts = posts.order_by('-date')[(4 * current_page) - 4:4 * current_page]

    if current_page > 2:
        lower_limit = current_page - 2
    else:
        lower_limit = 1

    if current_page < pages_number - 2:
        upper_limit = current_page + 2
    else:
        upper_limit = pages_number

    nav_pages = list(range(lower_limit, upper_limit + 1))

    context = {"author": author, "posts": posts, "current_page": current_page, "nav_pages": nav_pages,
               "pages_number": pages_number}

    return render(request, "author.html", context)
