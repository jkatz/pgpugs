from django.shortcuts import render_to_response

from pugs import PugGroups

# home page
def index(request):
    return render_to_response('index.html', {
        'pug_groups': PugGroups()
    })