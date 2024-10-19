from django.urls import path, include
from rest_framework import routers
from learning.views import CategoryViewSets, CourseViewSets, ModuleViewSets, ParentModuleViewSets, VideoViewSets

router = routers.DefaultRouter()
router.register('category', CategoryViewSets)
router.register('courses', CourseViewSets)
router.register('modules', ModuleViewSets)
router.register('videos', VideoViewSets)
router.register('parent-modules', ParentModuleViewSets)
urlpatterns = [
    path('', include(router.urls)),

]
