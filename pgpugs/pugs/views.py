from django.shortcuts import render_to_response
from django.template import RequestContext

from pugs import PugGroups, Posts

# home page
def index(request):
    return render_to_response('index.html', {
        'pug_groups': PugGroups(),
    }, RequestContext(request))

def posts(request):
    posts = Posts()
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    return render_to_response('posts/index.html', {
        'posts': posts.paginated(page)
    }, RequestContext(request))
