# Generated by Django 4.0.3 on 2022-03-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]