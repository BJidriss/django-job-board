# Generated by Django 3.0.6 on 2020-06-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_auto_20200605_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
