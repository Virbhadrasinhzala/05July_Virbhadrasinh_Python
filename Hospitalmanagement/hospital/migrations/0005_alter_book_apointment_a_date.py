# Generated by Django 4.1.3 on 2022-12-31 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_contact_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_apointment',
            name='a_date',
            field=models.DateField(),
        ),
    ]