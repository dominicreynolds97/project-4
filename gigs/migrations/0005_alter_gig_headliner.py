# Generated by Django 3.2.4 on 2021-06-13 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0005_auto_20210611_1237'),
        ('gigs', '0004_alter_gig_support_artists'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='headliner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='headliner', to='artists.artist'),
        ),
    ]
