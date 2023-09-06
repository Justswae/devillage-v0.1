from django.shortcuts import render, get_object_or_404
from .models import Posts


def Post(request):
    posts = Posts.objects.all()
    return render(request, 'templates/index.html',{
        'posts':posts
    })

def details(request, pk):
    post_detail = get_object_or_404(Posts,pk= pk)
    return render(request, 'templates/detail.html',
                  {'detail' : post_detail})

def about(request):
    return render(request, 'templates/about.html')

def contact(request):
    return render(request, 'templates/contact.html')