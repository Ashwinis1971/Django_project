from django.shortcuts import render
from . models import MovieInfo
# Create your views here.

def create(request):
    if request.POST:
        title = request.POST.get('title')
        year = request.POST.get('year')
        desc = request.POST.get('summary')
        movie_obj = MovieInfo(title=title, year=year, description=desc)
        movie_obj.save()

    return render(request, 'create.html')



def list(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    
    # list_movie_details = { 
    #                       'movies' : [
    #                       {
    #     'movie_name': 'nadana sambvan',
    #     'year': 2024,
    #     'sucess': True,
    #     'img': 'nadana_sam.jpeg'
    # },
      
    # {
    #     'movie_name': 'little heart',
    #     'year': 2024,
    #     'summary': 'Love movie',
    #     'sucess': True,
    #     'img': 'littlehearts.jpeg'
    # },  
    #  {
    #     'movie_name': 'Stree-2',
    #     'year': 2024,
    #     'summary': 'horror movie',
    #     'sucess': False,
    #     'img': 'stree2.jpeg'
    # }   ]          
    # }

    return render(request, 'list.html', {'movies': movie_set})



def edit(request):
    return render(request, 'edit.html')

    