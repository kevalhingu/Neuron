# Generated by Django 4.0.3 on 2023-03-31 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neuron_main', '0003_alter_doctor_photo_alter_story_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='avatar',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='badge',
            field=models.URLField(),
        ),
    ]
