from django.contrib import admin
from learning.models import (CategoryModel, CourseModel, ModuleModel,
                             VideoModel,
                             ParentModule
                             #  QuizModel,
                             #  ExamModel,
                             #  AnswerModel,
                             )


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('category', 'slug')  # Display slug in the admin panel


admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(CourseModel)
admin.site.register(ParentModule)


@admin.register(ModuleModel)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'parent_module', 'is_parent')
    search_fields = ('title', 'course__title')
    list_filter = ('is_parent',)


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
