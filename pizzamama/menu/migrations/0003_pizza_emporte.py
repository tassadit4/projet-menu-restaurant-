# Generated by Django 4.0.3 on 2022-03-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_pizza_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='emporte',
            field=models.BooleanField(default=False),
        ),
    ]
