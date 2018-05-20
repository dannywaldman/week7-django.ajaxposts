from django.shortcuts import render, HttpResponse
from .models import Post

def index(request):
    return render(request, 'posts/index.html')

def add(request):
    post = Post.objects.create(note = request.POST['post'])  
    print post 
    return HttpResponse(post.note)
    
