# Generated by Django 3.0.6 on 2020-05-09 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_google_maps.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geolocation', django_google_maps.fields.GeoLocationField(max_length=100)),
                ('address', django_google_maps.fields.AddressField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vessel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vesselLength', models.IntegerField()),
                ('vesselBreadth', models.IntegerField()),
                ('vesselMaxDraft', models.IntegerField()),
                ('vesselSpeed', models.IntegerField()),
                ('vesselName', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]