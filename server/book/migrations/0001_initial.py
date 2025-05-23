# Generated by Django 5.2.1 on 2025-05-08 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField()),
                ('title', models.CharField()),
                ('author', models.CharField()),
                ('genre', models.CharField()),
                ('published_date', models.CharField()),
                ('total_copies', models.CharField()),
                ('available_copies', models.CharField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
