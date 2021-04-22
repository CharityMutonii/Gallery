from django.contrib import admin
from .models import Photo, Location, Category

class PhotoAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

# Register your models here.

admin.site.register(Location)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(Category)