# Generated by Django 3.2.7 on 2021-10-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0003_author_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='decs',
            field=models.CharField(max_length=255),
        ),
    ]
