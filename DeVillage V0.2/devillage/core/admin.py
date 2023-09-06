from django.contrib import admin
from posts import models as md

admin.site.register(md.Category)
admin.site.register(md.Posts)
