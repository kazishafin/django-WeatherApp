# Generated by Django 3.1.4 on 2020-12-28 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0006_auto_20201228_1819'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['-id']},
        ),
    ]