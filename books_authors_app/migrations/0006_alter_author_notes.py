# Generated by Django 3.2.7 on 2021-10-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0005_rename_decs_book_decsription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='notes',
            field=models.CharField(max_length=255),
        ),
    ]
