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

class location(models.Model):
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
