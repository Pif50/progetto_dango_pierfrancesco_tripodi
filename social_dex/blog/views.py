from email import contentmanager
from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
from datetime import timedelta
from django.utils import timezone


def posts(response):
    response = []
    posts = Post.objects.filter().order_by('-datetime')
    for post in posts:
        response.append(
            {
                'title' : post.title,
                'content' : post.content,
                'datetime' : post.datetime,
                'author' : post.author.username,
                'hash': post.hash,
                'transaction ID': post.txId,
            }
        )


    return JsonResponse(response, safe = False)
