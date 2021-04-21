from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        '''
         method to display category
        '''
        return self.name
    def save_category(self):
        '''
         method to save category
        '''
        return self.save()
    def delete_category(self):
        '''
         method to delete category
        '''
        return self.delete()
    def update_category(self, cat1):
        '''
         method to update  category
        '''
        self.update(location_name = cat1)

class Location(models.Model):
        name = models.CharField(max_length=60)
        def __str__(self):
            '''
            method to update location
            '''
            return self.name
        def save_location(self):
            '''
            method to save location
            '''
            return self.save()
        def delete_location(self):
            '''
            method to delete location
            '''
            return self.delete()
        def update_location(self, loc1):
            '''
                method to update location
            '''
            self.update(location_name = loc1)

class Photo(models.Model):
    
    name = models.CharField(max_length=244)
    description = models.TextField()
    location = models.ForeignKey(Location)
    categories = models.ForeignKey(Category)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        '''
        method to display image
        '''
        return self.name
    def save_image(self):
        '''
        method to save image
        '''
        return self.save()
    def delete_image(self):
        '''
        method to delete image
        '''
        return self.delete()
   
