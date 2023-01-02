# Generated by Django 4.1.3 on 2022-12-24 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_book_apointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='d_signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('contact', models.BigIntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('pasword', models.CharField(max_length=50)),
            ],
        ),
    ]