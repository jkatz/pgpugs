from django.shortcuts import render_to_response

from pugs import PugGroups, Posts

# home page
def index(request):
    return render_to_response('index.html', {
        'pug_groups': PugGroups()
    })

def posts(request):
    posts = Posts()
    return render_to_response('posts/index.html', {
        'posts': posts.latest()
    })
