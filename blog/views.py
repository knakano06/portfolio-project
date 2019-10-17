# 'get_object_or_404' will either get the object (details for the specific blog)
# or send the user to 404 page, indicating that it could not get the information
from django.shortcuts import render, get_object_or_404

# access item in the Blog data base
from .models import Blog

def allblogs(request):
    # get the blog objects here and pass it back to uls.py using this render
    blogs = Blog.objects # list of blogs
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

# this function will get the information about the particular blog specified by
# blog_id and give it back to urls.py
def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog': detail_blog})
