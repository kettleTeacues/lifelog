# Generated by Django 4.1 on 2022-11-20 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifelog', '0008_alter_lifelog_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifelog',
            name='event',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
