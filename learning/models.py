from django.db import models
from django.utils.text import slugify


class CategoryModel(models.Model):
    category = models.CharField(max_length=40)
    slug = models.SlugField(max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category).replace('-', '_')
        super(CategoryModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.category


class LearningModel(models.Model):
    image = models.ImageField(upload_to='learning/uploads')
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.OneToOneField(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
