# Generated by Django 3.1.2 on 2020-10-24 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_community_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='listing',
        ),
        migrations.DeleteModel(
            name='Community',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]