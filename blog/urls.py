from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('posts/<int:post_id>', views.view_post, name='view_post'),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('author/<str:username>', views.view_author, name="view_author")
]
