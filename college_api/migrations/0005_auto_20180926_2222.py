# Generated by Django 2.1.1 on 2018-09-26 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('college_api', '0004_athletemedsession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=255)),
                ('user_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peroneals_rle', jsonfield.fields.JSONField()),
                ('peroneals_lle', jsonfield.fields.JSONField()),
                ('med_gastro_lle', jsonfield.fields.JSONField()),
                ('med_gastro_rle', jsonfield.fields.JSONField()),
                ('tib_anterior_lle', jsonfield.fields.JSONField()),
                ('tib_anterior_rle', jsonfield.fields.JSONField()),
                ('lat_gastro_lle', jsonfield.fields.JSONField()),
                ('lat_gastro_rle', jsonfield.fields.JSONField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('assessment', models.TextField()),
                ('treatment', models.TextField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_api.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_api.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='trainer_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
