from django.contrib import admin
from .models import Actor, RatingStar, Genre, Category, Movie, MovieShots, Rating, Reviews
from django.utils.html import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Categories"""
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class ReviewInline(admin.TabularInline):
    """Review on movie page"""
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')
    get_image.short_description = "Image"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Movies"""
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInline, ReviewInline,]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", "poster", "get_image")
        }),
        (None, {
            "fields": (("year", "world_premiere", "country"),)
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("actors", "directors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Options", {
            "fields": (("url", "draft"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')
    get_image.short_description = "Poster"


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Review"""
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genre"""
    list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Actors"""
    list_display = ("name", "age", "get_image")
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"')
    get_image.short_description = "Image"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Rating"""
    list_display = ("ip",)


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """Movie Shouts"""
    list_display = ("title", "movie", 'get_image')

    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50"')
    get_image.short_description = "Image"


admin.site.register(RatingStar)


admin.site.site_header = "XMovies"