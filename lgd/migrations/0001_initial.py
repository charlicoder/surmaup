# Generated by Django 3.0.5 on 2020-05-03 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zila',
            fields=[
                ('zila_flid', models.CharField(default=570, editable=False, max_length=4, primary_key=True, serialize=False)),
                ('zila_geocode', models.CharField(max_length=2)),
                ('division_geocode', models.CharField(max_length=2)),
                ('zila_name_en', models.CharField(blank=True, max_length=30, null=True)),
                ('zila_name_bn', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upazila',
            fields=[
                ('upazila_flid', models.CharField(default=239, editable=False, max_length=6, primary_key=True, serialize=False)),
                ('upazila_geocode', models.CharField(max_length=2)),
                ('upazila_name_en', models.CharField(blank=True, max_length=30, null=True)),
                ('upazila_name_bn', models.CharField(blank=True, max_length=30, null=True)),
                ('zila', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lgd.Zila')),
            ],
        ),
    ]
