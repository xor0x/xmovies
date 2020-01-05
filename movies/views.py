from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Movie
from django.views.generic import ListView, DetailView
from .forms import ReviewForm


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    model = Movie
    slug_field = "url"


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie_id = pk
            form.save()
        return redirect(movie.get_absolute_url())
