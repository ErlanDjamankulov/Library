from django.contrib import admin
from .models import *

admin.site.register(Publisher)
admin.site.register(Language)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookPhoto)
admin.site.register(AuthorPhoto)