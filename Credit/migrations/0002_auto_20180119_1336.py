# Generated by Django 2.0.1 on 2018-01-19 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Credit', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='credit',
            unique_together={('appId', 'userId')},
        ),
    ]