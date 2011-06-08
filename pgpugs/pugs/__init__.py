from pugs.models import Region

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