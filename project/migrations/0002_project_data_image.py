# Generated by Django 3.0.3 on 2020-08-09 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_data',
            name='image',
            field=models.FileField(default=2, upload_to='project_image/'),
            preserve_default=False,
        ),
    ]
