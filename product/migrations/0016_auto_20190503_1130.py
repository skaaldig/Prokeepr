# Generated by Django 2.0.13 on 2019-05-03 15:30

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_auto_20190502_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinstance',
            name='rental_end',
            field=models.DateField(validators=[product.models.future_dates_only]),
        ),
    ]
