# Generated by Django 3.1.3 on 2020-12-15 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_note_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_note',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
