from django.urls import path, include
from rest_framework import routers
from learning.views import CategoryViewSets

router = routers.DefaultRouter()
router.register('category', CategoryViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
