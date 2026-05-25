from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Category, Blog

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    posts = Blog.objects.filter(status='Published').order_by('-created_at')



    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,

    }

    return render(request, "home.html", context)


def favicon(request):
        svg = """<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'>
    <rect width='64' height='64' rx='14' fill='#111827'/>
    <path d='M18 22h28v6H18zm0 10h28v6H18zm0 10h18v6H18z' fill='#f59e0b'/>
</svg>"""
        return HttpResponse(svg, content_type='image/svg+xml')