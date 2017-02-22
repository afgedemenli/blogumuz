from django.shortcuts import render, get_object_or_404
from .models import Blog,Comment
from django.contrib.auth.models import User

def main(request):
    all_blogs = Blog.objects.all()
    return render(request,"index.html",{'all_blogs' : all_blogs})

def display(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        comment = Comment(text=request.POST.get('txt','anan'),user=request.user,blog=blog,title="comment")
        comment.save()
    comments = blog.comment_set.all()
    return render(request,"display.html",{'blog' : blog, 'comments':comments})
