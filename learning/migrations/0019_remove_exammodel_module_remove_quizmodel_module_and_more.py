# Generated by Django 5.1.2 on 2024-10-19 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0018_parentmodule_alter_modulemodel_parent_module'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exammodel',
            name='module',
        ),
        migrations.RemoveField(
            model_name='quizmodel',
            name='module',
        ),
        migrations.DeleteModel(
            name='AnswerModel',
        ),
        migrations.DeleteModel(
            name='ExamModel',
        ),
        migrations.DeleteModel(
            name='QuizModel',
        ),
    ]
