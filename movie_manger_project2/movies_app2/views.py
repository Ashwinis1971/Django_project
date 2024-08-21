from django.shortcuts import render

# Create your views here.

def create(request):
    if request.POST:
        title = request.POST.get('title')
        year = request.POST.get('year')
        summary = request.POST.get('summary')
        
        print(f"Title: {title}\nYear: {year}\nSummary: {summary}")

    return render(request, 'create.html')



def list(request):
    list_movie_details = { 
                          'movies' : [
                          {
        'movie_name': 'nadana sambvan',
        'year': 2024,
        'sucess': True,
        'img': 'nadana_sam.jpeg'
    },
      
    {
        'movie_name': 'little heart',
        'year': 2024,
        'summary': 'Love movie',
        'sucess': True,
        'img': 'littlehearts.jpeg'
    },  
     {
        'movie_name': 'Stree-2',
        'year': 2024,
        'summary': 'horror movie',
        'sucess': False,
        'img': 'stree2.jpeg'
    }   ]          
    }

    return render(request, 'list.html', list_movie_details)



def edit(request):
    return render(request, 'edit.html')

    