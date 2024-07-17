from django.db import models
from artmart_backend.users.models import User

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
    artist = models.ForeignKey(Details, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    upload_date_time = models.DateTimeField(auto_now_add=True)
    ar_model_ref = models.FileField()
    
    AVAILABILITY_CHOICES = [
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    ]
    
    availability = models.CharField(max_length=50, choices=AVAILABILITY_CHOICES)

    def __str__(self):
        return self.title

