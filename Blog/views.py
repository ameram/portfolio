from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def gen_show(request):
    my_blog = Blog.objects
    return render(request, 'blog/general.html', {'blogs': my_blog})


def detail(request, blog_id):
    blog_object = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'Blog/detail.html', {'blog':blog_object})
