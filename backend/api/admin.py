from django.contrib import admin

from . models import Profile,Rating,Movie,KmeansResult,Subscribe
from . models import Profile,Rating,Movie,KmeansResult,MoviePoster,Subscribe,Poster


admin.site.register(Profile)
admin.site.register(Rating)
admin.site.register(Movie)
admin.site.register(KmeansResult)

admin.site.register(MoviePoster)
admin.site.register(Subscribe)
admin.site.register(Poster)
