from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("create/", views.create_blog, name='create_blog'),
    path("update/<int:pk>/", views.update_blog, name='update_blog'),
    path('contacts/', views.contacts, name='contacts'),
]