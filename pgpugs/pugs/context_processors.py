from pugs import Posts

def latest_posts(request):
    return { 'latest_posts': Posts().latest() }
    