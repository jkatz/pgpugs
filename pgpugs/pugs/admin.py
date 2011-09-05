from django.contrib import admin
from models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title', ) }

admin.site.register(Country)
admin.site.register(Post, PostAdmin)
admin.site.register(Pug)
admin.site.register(Region)
admin.site.register(PugAuthor)
