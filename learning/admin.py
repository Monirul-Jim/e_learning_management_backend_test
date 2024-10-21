from django.contrib import admin
from learning.models import (CategoryModel, CourseModel, ModuleModel,
                             VideoModel,
                             ParentModule
                             #  QuizModel,
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


# # Registering QuizModel
# @admin.register(QuizModel)
# class QuizAdmin(admin.ModelAdmin):
#     list_display = ('title', 'module')
#     search_fields = ('title', 'module__title')


# # Registering ExamModel
# @admin.register(ExamModel)
# class ExamAdmin(admin.ModelAdmin):
#     list_display = ('title', 'module', 'submission_deadline')
#     search_fields = ('title', 'module__title')


# # Registering AnswerModel
# @admin.register(AnswerModel)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('user', 'exam', 'submitted_at')
#     search_fields = ('user__username', 'exam__title')
#     readonly_fields = ('submitted_at',)
