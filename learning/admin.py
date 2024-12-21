from django.contrib import admin
from learning.models import (CategoryModel, CourseModel, ModuleModel,
                             VideoModel,
                             ParentModule,
                             QuizModel,
                             #  ExamModel,
                             #  AnswerModel,
                             )


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')


admin.site.register(CourseModel)
admin.site.register(ParentModule)


@admin.register(ModuleModel)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'parent_module')
    search_fields = ('title', 'course__title')


# Registering VideoModel
@admin.register(VideoModel)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'video_url')
    search_fields = ('title', 'module__title')


@admin.register(QuizModel)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'module']
