# Generated by Django 3.1.3 on 2020-12-15 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_sub_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]