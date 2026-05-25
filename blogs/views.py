from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):

    posts = Blog.objects.filter(category=category_id, status = 'Published')
    try:
        category = Category.objects.get(id=category_id)
    except:
        return redirect('home')

    # category = get_object_or_404(Category, id=category_id)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)