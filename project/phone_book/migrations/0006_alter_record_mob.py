# Generated by Django 4.2.7 on 2023-11-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book', '0005_alter_record_mob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='mob',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
