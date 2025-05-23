# Generated by Django 5.2 on 2025-05-01 15:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=250)),
                ('icone', models.CharField(max_length=250, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]
