# Generated by Django 3.2 on 2022-07-18 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220718_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='subject',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
