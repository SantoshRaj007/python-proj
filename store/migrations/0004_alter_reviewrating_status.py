# Generated by Django 5.1.2 on 2025-05-05 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
