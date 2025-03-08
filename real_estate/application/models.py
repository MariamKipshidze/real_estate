from django.db import models


class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('land', 'Land'),
        ('commercial', 'Commercial'),
    ]

    # Property Fields
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)  # Price of the property
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, default='house')  # Type of the property
    location = models.CharField(max_length=255)  # Location (address) of the property
    created_at = models.DateTimeField(auto_now_add=True)  # Date the property was created
    updated_at = models.DateTimeField(auto_now=True)  # Date the property was last updated

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    # Image field for storing property images
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.property.title}"
