from django.shortcuts import render
from .models import Photo, Location,Category
# Create your views here.

def index(request):
    photos = Photo.all_photos()
    return render(request, "index.html", {'photos':photos})


