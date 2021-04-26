from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
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

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name
    def save_location(self):

        return self.save()
    def delete_location(self):
        return self.delete()
    def update_location(self, loc1):

        self.update(location_name = loc1)

class Photo(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=244)
    description = models.TextField()
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
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

    @classmethod
    def all_photos(cls):
        """
        A method to return all photos
        """
        return cls.objects.all()

    @classmethod
    def get_photo_by_id(cls, id):
        """
        A method to get a photo based on its id
        """
        return cls.objects.get(id = id)

    @classmethod
    def search_photo_by_category(cls, search):
        """
        A method to return all photos based on catergory
        """
        return cls.objects.filter(category__name__icontains = search)
        
    @classmethod
    def filter_by_location(cls, location):
        """
        A method to filter all photos based on the location
        """
        return cls.objects.filter(location__name__icontains = location)    