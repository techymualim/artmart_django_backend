from django.db import models
from artmart_backend.users.models import User
import os
from django.core.exceptions import ValidationError

def validate_file_type(value):
    
    valid_extensions = ['.glb', '.gltf']  # Add valid extensions
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported file extension.')
    
   
    
def validate_image_file_type(value):
    valid_image_mime_types = ['image/jpeg', 'image/png']  # Add valid MIME types
    valid_image_extensions = ['.jpg', '.jpeg', '.png']  # Add valid extensions
    ext = os.path.splitext(value.name)[1]
    if ext.lower() not in valid_image_extensions:
        raise ValidationError('Unsupported image file extension.')
    
    # Optionally check the MIME type if needed
    if value.file.content_type not in valid_image_mime_types:
        raise ValidationError('Unsupported image file type.')

class Details(models.Model):
    SHOP_TYPE_CHOICES = [
        ('INDIVIDUAL', 'Individual'),
        ('TRADER_BUSINESS', 'Trader Business'),
    ]

    ART_SPECIALIZATION_CHOICES = [
        ('PAINTING', 'Painting'),
        ('JEWELLERY', 'Jewellery'),
        ('POTTERY', 'Pottery'),
        ('DECORATION', 'Decoration'),
        ('OTHER', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller_details')
    store_name = models.CharField(max_length=255)
    store_email = models.EmailField()
    address = models.TextField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=255)
    shop_address = models.CharField(max_length=255, blank=True, null=True)
    shop_city = models.CharField(max_length=255, blank=True, null=True)
    shop_state = models.CharField(max_length=255, blank=True, null=True)
    shop_postal_code = models.CharField(max_length=50, blank=True, null=True)
    shop_country = models.CharField(max_length=255, blank=True, null=True)
    shop_type = models.CharField(max_length=50, choices=SHOP_TYPE_CHOICES, blank=True, null=True)
    art_specialization = models.CharField(max_length=50, choices=ART_SPECIALIZATION_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.store_name
    

    
class Product(models.Model):
    
    PRODUCT_CHOICES = [
        ('PAINTING', 'Painting'),
        ('JEWELLERY', 'Jewellery'),
        ('POTTERY', 'Pottery'),
        ('DECORATION', 'Decoration')
    ]
    
    artist = models.ForeignKey(Details, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    upload_date_time = models.DateTimeField(auto_now_add=True)
    ar_model_ref = models.FileField(upload_to='ar_models/', validators=[validate_file_type])
    ar_model_image = models.ImageField(upload_to='ar_model_images/', validators=[validate_image_file_type])
    category=models.CharField(max_length=255,choices=PRODUCT_CHOICES,default="PAINTING")
    
    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]
    
    availability = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES)

    def __str__(self):
        return self.title

