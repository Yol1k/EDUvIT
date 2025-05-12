from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from .models import Blog, Comment
from .forms import BlogModelForm, CommentModelForm

def index(request):
    blogs = Blog.objects.all().order_by('-date_published')
    search = request.GET.get('search')

    if search:
        blogs = blogs.filter(title__icontains=search)

    paginator = Paginator(blogs,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    title = "Главная страница"
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj, 'title': title})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comments = Comment.objects.filter(blog=blog).order_by('-date_published')
    title = blog.title
    form = CommentModelForm()

    if 'post' in request.GET:
        all_blogs = Blog.objects.order_by('id')
        current_index = list(all_blogs.values_list('id', flat=True)).index(blog.id)
        
        if request.GET.get('post') == "prev":
            prev_index = current_index - 1 if current_index > 0 else len(all_blogs) - 1
            return redirect("blog:blog_detail", pk=all_blogs[prev_index].id)
        
        elif request.GET.get('post') == "next":
            next_index = current_index + 1 if current_index < len(all_blogs) - 1 else 0
            return redirect("blog:blog_detail", pk=all_blogs[next_index].id)

    context = {
        "blog": blog,
        "title": title,
        "comments": comments
    }

    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.date_published = datetime.now()
            new_comment.blog = blog
            new_comment.save()
            return redirect("blog:blog_detail", pk=pk)
    else:
        form = CommentModelForm()
    context["form"] = form
    return render(request, 'blog/blog_detail.html', context)

def create_blog(request):
    title = "Создание блога"
    action = "Создать"
    if request.method == "POST":
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.date_published = datetime.now()
            new_blog.save()
            return redirect("blog:index")
    else:
        form = BlogModelForm()
    return render(request, 'blog/create_update_blog.html', {'title':title, 'form':form, 'action':action})

def update_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    action = "Обновить"
    title = f"Редактирование {blog.title}"
    if request.method == "POST":
        form = BlogModelForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("blog:blog_detail",pk=pk)
    else:
        form = BlogModelForm(instance=blog)
    return render(request, 'blog/create_update_blog.html', {'title':title, 'form':form, 'action':action})

def contacts(request):
    title = "Контакты"
    return render(request, 'blog/contacts.html', {'title':title})
