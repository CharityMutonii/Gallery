from django.shortcuts import render
from .models import Photo, Location,Category
# Create your views here.

def index(request):
    photos = Photo.all_photos()
    return render(request, "index.html", {'photos':photos})

  
def search_results(request):
    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Image.search_by_name(search_term)
        print("searched_photos")
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})      

