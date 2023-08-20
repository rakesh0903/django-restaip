from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp1.models import Movie

# Create your views here.

#---------------------------------------
# def movie_list(request):
#     movies = Movie.objects.all()

#     return HttpResponse(movies.values())

#---------------------------------------

def movie_list(request):
    movies = Movie.objects.all().values() 

    data ={
        'movies':list(movies)
    }
    
    return JsonResponse(data)

#---------------------------------------

def movie_details(request,pk):
    movie = Movie.objects.get(pk=pk)

    data={
        'movie':movie.name,
        'description':movie.descriptios,
        'active':movie.active
    }

    return JsonResponse(data)
    