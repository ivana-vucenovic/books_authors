# Generated by Django 3.2.7 on 2021-10-13 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0004_alter_book_decs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='decs',
            new_name='decsription',
        ),
    ]
