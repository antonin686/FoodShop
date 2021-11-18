from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="images/")
    cover_image = models.ImageField(upload_to="images/")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    AVAILABILITY_CHOICES = [
        (0, 'NO'),
        (1, 'YES'),
    ]
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.ImageField(upload_to="images/")
    availability = models.SmallIntegerField(choices=AVAILABILITY_CHOICES, default=1)
    category = models.ForeignKey(Collection, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name