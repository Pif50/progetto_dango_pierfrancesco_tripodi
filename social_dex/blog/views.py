from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse, HttpResponseNotFound
from datetime import timedelta

from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def nuovo_articolo(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
        
            post = form.save(commit=False)
            post.author = request.user
            post.post_date = timezone.now()
            
            if 'hack' in post.content: 
                return HttpResponseNotFound('There is a no valid word in the post content!')
            
            #L'articolo verrà scritto sulla Blockchain
            post.write_on_chain()
            print('content written in Block successfuly')
            post.save()
            return redirect('homepage')
    else:
        form = PostForm()

        context = {
            'form': form
        }

    return render(request, 'blog/nuovo_articolo.html', context)

    

def hash_txid(response):
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
