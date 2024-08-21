from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def print_hello(request):
    # return HttpResponse('<b>hello django<b>')
    list_movie_details = { 
                          'movies' : [
                          {
        'movie_name': 'nadana sambvan',
        'year': 2024,
        'sucess': True
    },
      
    {
        'movie_name': 'little heart',
        'year': 2024,
        'summary': 'Love movie',
        'sucess': True
    },  
     {
        'movie_name': 'Shree-2',
        'year': 2024,
        'summary': 'horror movie',
        'sucess': False
    }   ]          
    }
    
    return render(request, 'index.html', list_movie_details)


