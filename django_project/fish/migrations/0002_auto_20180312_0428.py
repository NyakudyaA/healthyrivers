# Generated by Django 2.0.2 on 2018-03-12 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxon',
            name='iucn_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fish.IUCNStatus'),
        ),
    ]
