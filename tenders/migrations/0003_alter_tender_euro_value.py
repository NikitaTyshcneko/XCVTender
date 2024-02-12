# Generated by Django 4.2.10 on 2024-02-12 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenders', '0002_tender_tender_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tender',
            name='euro_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
