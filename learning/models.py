from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class CategoryModel(models.Model):
    category = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category).replace('-', '_')
        super(CategoryModel, self).save(*args, **kwargs)

    def clean(self):
        if CategoryModel.objects.filter(category=self.category).exists():
            raise ValidationError(
                f'The category "{self.category}" already exists.')

    def __str__(self):
        return self.category


class CourseModel(models.Model):
    image = models.URLField(max_length=500)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(blank=True, null=True)
    categories = models.ManyToManyField('CategoryModel')

    def clean(self):
        if self.price is not None and self.price < 0:
            raise ValidationError({'price': "Price cannot be negative."})

    def __str__(self):
        return self.title
