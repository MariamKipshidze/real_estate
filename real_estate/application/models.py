from django.db import models


class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condo'),
        ('land', 'Land'),
        ('commercial', 'Commercial'),
    ]

    agent = models.ForeignKey(
        to="user.CustomUser",
        verbose_name="Agent",
        on_delete=models.CASCADE,
        blank=True, null=True
    )

    title = models.CharField(verbose_name="Title", max_length=255)
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(verbose_name="Price", max_digits=12, decimal_places=2)
    area = models.DecimalField(
        verbose_name="Area",
        max_digits=10,
        decimal_places=2,
        help_text="Area in square meters",
        default=0
    )
    property_type = models.CharField(
        verbose_name="Property type", max_length=20, choices=PROPERTY_TYPES, default='house')
    location = models.CharField(verbose_name="Location", max_length=255)
    number_of_rooms = models.PositiveIntegerField(verbose_name="Number of rooms", default=1)
    floor = models.PositiveIntegerField(verbose_name="Floor", default=1)
    has_lift = models.BooleanField(verbose_name="Has lift", default=False)
    central_heating = models.BooleanField(verbose_name="Central heating", default=False)

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"
        ordering = ['-created_at']

    @property
    def price_per_square_meter(self):
        if hasattr(self, 'size') and self.area > 0:
            return self.price / self.area
        return 0


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Image for {self.property.title}"

    class Meta:
        verbose_name = "Property Image"
        verbose_name_plural = "Property Images"
