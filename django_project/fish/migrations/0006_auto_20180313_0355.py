# Generated by Django 2.0.2 on 2018-03-13 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0005_auto_20180312_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxon',
            name='iucn_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fish.IUCNStatus'),
        ),
    ]
