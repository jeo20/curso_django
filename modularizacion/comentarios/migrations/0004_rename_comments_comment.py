# Generated by Django 5.0.2 on 2024-03-13 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_comments_signature'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comments',
            new_name='Comment',
        ),
    ]
