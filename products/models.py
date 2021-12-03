from django.db import models
from django.core.files import File
from io import BytesIO
from PIL import Image


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.slug}/"


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="uploads/", blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("-date_added",)  # Order in decending

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.slug}/"

    def get_image(self):
        if self.image:
            return BASE_URL + self.image.url
        else:
            return ""

    def get_thumbnail(self):
        if self.thumbnail:
            return BASE_URL + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return BASE_URL + self.thumbnail.url
            else:
                return ""

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert("RGBA")
        img.thumbnail(size)
        thumb_IO = BytesIO()
        img.save(thumb_IO, "JPEG", quality=85)
        thumbnail = File(thumb_IO, name=image.name)
        return thumbnail
