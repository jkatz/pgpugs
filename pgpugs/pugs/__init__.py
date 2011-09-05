from django.core.paginator import Paginator, InvalidPage, EmptyPage

from pugs.models import Post, Region

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

    def paginated(self, page):
        """
            return a paginated set of results for blog posts
            defaults to the first page, which will be the latest results
        """
        posts = Post.objects.order_by('-date_published')
        paginator = Paginator(posts, 10)

        try:
            return paginator.page(page)
        except (EmptyPage, InvalidPage):
            return paginator.page(1)

    def latest(self):
        return Post.objects.order_by('-date_published')[:5]
