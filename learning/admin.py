from django.contrib import admin
from learning.models import CategoryModel, CourseModel


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')  # Display slug in the admin panel


admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(CourseModel)
