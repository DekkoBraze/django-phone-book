# Generated by Django 4.2.7 on 2023-11-24 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book', '0003_alter_record_house_alter_record_korp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='mob',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]