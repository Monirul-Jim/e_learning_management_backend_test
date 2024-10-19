# Generated by Django 5.1.2 on 2024-10-19 16:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0016_remove_order_items_delete_cartitem_delete_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('instructions', models.TextField(blank=True)),
                ('submission_deadline', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(help_text="User's answer submission")),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='learning.exammodel')),
            ],
        ),
        migrations.CreateModel(
            name='ModuleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_parent', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='learning.coursemodel')),
                ('parent_module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_modules', to='learning.modulemodel')),
            ],
        ),
        migrations.AddField(
            model_name='exammodel',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='learning.modulemodel'),
        ),
        migrations.CreateModel(
            name='QuizModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('questions', models.TextField(blank=True, help_text='List questions in plain text or JSON format')),
                ('module', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='learning.modulemodel')),
            ],
        ),
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video_url', models.URLField(max_length=500)),
                ('duration', models.DurationField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='learning.modulemodel')),
            ],
        ),
    ]