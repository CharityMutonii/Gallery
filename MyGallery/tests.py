from django.test import TestCase
from .models import Photo,Location,Category

# Create your tests here.
class PhotoTestClass(TestCase):
    
     # Set up method
    def setUp(self):
        self.photo1= Photo(name = 'boy', description ='boy pic')
        self.place = Location(name = "Kigali")
        self.place.save()

        self.category = Category(name = "people")
        self.category.save()  
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.photo1, Photo))
        
    # Testing Save Method
    def test_save_method(self):
        self.photo1.save_image()
        photos = Photo.objects.all()
        self.assertTrue(len(photos) > 0)
        
    # Testing delete Method
    def test_delete_method(self):
        self.photo1.save_image()
        photo = Photo.objects.filter(name='boy').first()
        delete=Photo.objects.filter(name=photo.name).delete()
        photos=Photo.objects.all()
        self.assertTrue(len(photos) == 0) 

     # Testing update Method
    def test_update_method(self):
        self.photo1.save_image()
        photo = Photo.objects.filter(name='boy').first()
        update=Photo.objects.filter(id=photo.id).update(name="zebra")
        updated= Photo.objects.filter(name="zebra").first()
        self.assertTrue(photo.name,updated.name)    
    def test_get_photo_by_id(self):
        photo1 = Photo.get_photo_by_id(self.photo1.id)
        self.assertEqual(photo1, self.photo1)

    def test_search_photo_by_category(self):
        photos = Photo.search_photo_by_category("people")
        self.assertFalse(len(photos) > 0)

    def test_filter_by_location(self):
        photos = Photo.filter_by_location(self.location.name)
        self.assertTrue(len(photos) > 0)    
# Location test

class LocationTestClass(TestCase):
    
     # Set up method
    def setUp(self):
        self.location1= Location(location_name = 'kigali')
            
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location1, Location))
        
    # Testing Save Method
    def test_save_method(self):
        self.location1.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
        
    # Testing delete Method
    def test_delete_method(self):
        self.location1.save_location()
        location = Location.objects.filter(location_name = 'kigali').first()
        delete=Location.objects.filter(location_name=location.location_name).delete()
        locations=Location.objects.all()
        self.assertTrue(len(locations) == 0) 

    
     # Testing update Method
    def test_update_method(self):
        self.location1.save_location()
        location = Location.objects.filter(location_name = 'kigali').first()
        update=Location.objects.filter(id=location.id).update(location_name="musanze")
        updated= Location.objects.filter(location_name="musanze").first()
        self.assertTrue(location.location_name,updated.location_name)    

# category test
class CategoryTestClass(TestCase):
    
     # Set up method
    def setUp(self):
        self.category1= Category(name = 'people')
            
    
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category1, Category))
        
    # Testing Save Method
    def test_save_method(self):
        self.category1.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
        
    # Testing delete Method
    def test_delete_method(self):
        self.category1.save_category()
        category = Category.objects.filter(name = 'people').first()
        delete=Category.objects.filter(name=Category.name).delete()
        categories=Category.objects.all()
        self.assertFalse(len(categories) == 0)  

    # Testing update Method
    def test_update_method(self):
        self.category1.save_category()
        category = Category.objects.filter(name = 'people').first()
        update=Category.objects.filter(id=category.id).update(name="Animals")
        updated= Category.objects.filter(name="Animals").first()
        self.assertTrue(category.name,updated.name) 