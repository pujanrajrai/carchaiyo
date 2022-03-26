# Generated by Django 4.0.3 on 2022-03-24 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='cars.transmission'),
            preserve_default=False,
        ),
    ]