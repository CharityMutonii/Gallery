from django.shortcuts import render
from .models import Photo, Location,Category
# Create your views here.

def index(request):
    photos = Photo.all_photos()
    return render(request, "index.html", {'photos':photos})

  
def search_results(request):
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_photo_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})      

def display_location(request,location):
    
        locat=Photo.filter_by_location(location)
        print(locat)
        location=Location.objects.all()
       
    
        return render(request,'location.html',{'location':location, 'photo':locat}) 