# Generated by Django 4.0.3 on 2023-03-31 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.URLField()),
                ('name', models.CharField(max_length=30)),
                ('portfolio', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=15)),
                ('range', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('primary', models.CharField(max_length=10)),
                ('secondary_url', models.CharField(max_length=35)),
                ('range', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='SolutionAsUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('primary', models.CharField(max_length=60)),
                ('range', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('topic', models.CharField(max_length=10)),
                ('primary', models.CharField(max_length=35)),
                ('paragraph', models.TextField()),
                ('range', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angry', models.FloatField(default=0.0)),
                ('fear', models.FloatField(default=0.0)),
                ('happy', models.FloatField(default=0.0)),
                ('sad', models.FloatField(default=0.0)),
                ('surprise', models.FloatField(default=0.0)),
                ('at', models.DateTimeField(auto_now_add=True)),
                ('target_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]