# Generated by Django 5.0.2 on 2024-08-26 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0003_comments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='signature',
            field=models.CharField(default='Firma', max_length=100),
        ),
    ]
