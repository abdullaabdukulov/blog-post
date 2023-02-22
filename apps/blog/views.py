from django.shortcuts import render


def home(request):
    return render(request, 'blog.html')


def blog_single(request):
    return render(request, 'single.html')