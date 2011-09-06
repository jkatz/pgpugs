from django.contrib import admin
from models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('title', ) }

class PugAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug': ('name', ) }

admin.site.register(Country)
admin.site.register(Post, PostAdmin)
admin.site.register(Pug)
admin.site.register(Region)
admin.site.register(PugAuthor)
