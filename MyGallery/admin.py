from django.contrib import admin
from .models import Photo, Location, Category

class PhotoAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "location", "category","post_date"]
    class Meta:
        model = Photo
# Register your models here.
admin.site.register(Location)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(Category)