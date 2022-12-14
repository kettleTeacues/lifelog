# Generated by Django 4.1 on 2022-12-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifelog', '0011_remove_lifelog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifelog',
            name='endDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='lifelog',
            name='staDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddConstraint(
            model_name='lifelog',
            constraint=models.UniqueConstraint(fields=('staDate', 'endDate', 'event', 'created_by'), name='unique_log'),
        ),
    ]
