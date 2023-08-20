from django.urls import path 
from myapp1 import views

urlpatterns =[
    path('list/',views.movie_list,name='movie_list'),

]