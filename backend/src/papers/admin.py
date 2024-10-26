from django.contrib import admin

from .models import Paper, Author, Journal, PaperDistance

admin.site.register(Paper)
admin.site.register(Author)
admin.site.register(Journal)
admin.site.register(PaperDistance)
