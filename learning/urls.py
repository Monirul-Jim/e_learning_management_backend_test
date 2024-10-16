from django.urls import path, include
from rest_framework import routers
from learning.views import CategoryViewSets, CourseViewSets

router = routers.DefaultRouter()
router.register('category', CategoryViewSets)
router.register('courses', CourseViewSets)
urlpatterns = [
    path('', include(router.urls)),
]
