from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


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


class ParentModule(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class ModuleModel(models.Model):
    course = models.ForeignKey(
        CourseModel, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=100)
    parent_module = models.ForeignKey(
        ParentModule, on_delete=models.CASCADE, null=True, blank=True, related_name='child_modules')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class VideoModel(models.Model):
    module = models.ForeignKey(
        ModuleModel, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=100)
    video_url = models.URLField(max_length=500)
    duration = models.DurationField()

    def __str__(self):
        return self.title


class QuizModel(models.Model):
    module = models.ForeignKey(
        ModuleModel, on_delete=models.CASCADE, related_name='quizzes', null=True, blank=True)
    title = models.CharField(max_length=100)
    questions = models.JSONField(
        help_text="Stores the question, options, and correct answer in JSON format", blank=True, null=True
    )

    def __str__(self):
        return self.title
