from django.urls import path, include
from rest_framework import routers
from learning.views import CategoryViewSets, CourseViewSets, ModuleViewSets, ParentModuleViewSets, VideoViewSets, QuizViewSets

router = routers.DefaultRouter()
router.register('category', CategoryViewSets)
router.register('courses', CourseViewSets)
router.register('modules', ModuleViewSets)
router.register('videos', VideoViewSets)
router.register('parent-modules', ParentModuleViewSets)
router.register('quizzes', QuizViewSets, basename='quiz')

urlpatterns = [
    path('', include(router.urls)),

]
