# Generated by Django 4.0.3 on 2023-03-31 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neuron_main', '0006_remove_story_redirect_url_doctor_redirect_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='redirect_url',
        ),
        migrations.AddField(
            model_name='game',
            name='redirect_url',
            field=models.URLField(default='https://supermarioplay.com/'),
        ),
    ]