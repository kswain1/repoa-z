# Generated by Django 2.1.1 on 2019-01-18 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('college_api', '0028_athletemedsession_user_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='MVC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tib_anterior_lle', models.FloatField(blank=True, null=True)),
                ('tib_anterior_rle', models.FloatField(blank=True, null=True)),
                ('med_gastro_rle', models.FloatField(blank=True, null=True)),
                ('med_gastro_lle', models.FloatField(blank=True, null=True)),
                ('peroneals_lle', models.FloatField(blank=True, null=True)),
                ('lat_gastro_lle', models.FloatField(blank=True, null=True)),
                ('lat_gastro_rle', models.FloatField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('player_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_api.Player')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MVCLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tib_anterior_lle', jsonfield.fields.JSONField(blank=True, null=True)),
                ('tib_anterior_rle', jsonfield.fields.JSONField(blank=True, null=True)),
                ('med_gastro_rle', jsonfield.fields.JSONField(blank=True, null=True)),
                ('med_gastro_lle', jsonfield.fields.JSONField(blank=True, null=True)),
                ('peroneals_lle', jsonfield.fields.JSONField(blank=True, null=True)),
                ('lat_gastro_lle', jsonfield.fields.JSONField(blank=True, null=True)),
                ('lat_gastro_rle', jsonfield.fields.JSONField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('player_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_api.Player')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='athletemedsession',
            name='assessment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='athletemedsession',
            name='treatment',
            field=models.TextField(blank=True, null=True),
        ),
    ]