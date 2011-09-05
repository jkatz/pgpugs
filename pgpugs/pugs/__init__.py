from pugs.models import Region
from pugs.models import Post

class PugGroups():
    def africa(self):
        return Region.objects.get(slug='africa')

    def europe(self):
        return Region.objects.get(slug='europe')

    def north_america(self):
        return Region.objects.get(slug='northamerica')

    def south_america(self):
        return Region.objects.get(slug='southamerica')

    def oceania(self):
        return Region.objects.get(slug='oceania')

class Posts():

    def latest(self):
        return Post.objects.order_by('-date_published')[:5]
