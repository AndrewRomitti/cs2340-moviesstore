from django.shortcuts import render
from .models import Movie
# Create your views here.

def index(request):
    template_data = {}
    template_data['title'] = 'Movies'
    template_data['movies'] = Movie.objects.all()
    return render(request, 'movies/index.html',
                  {'template_data': template_data})

def show(request, id):
    movie = Movie.objects.get(id=id)
    template_data = {}
    template_data['title'] = movie.name
    template_data['movie'] = movie
    return render(request, 'movies/show.html',
                  {'template_data': template_data})