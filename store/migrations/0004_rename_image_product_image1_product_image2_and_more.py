# Generated by Django 4.1.6 on 2023-07-09 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_category_id_alter_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='', upload_to='upload/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='', upload_to='upload/products'),
        ),
    ]
