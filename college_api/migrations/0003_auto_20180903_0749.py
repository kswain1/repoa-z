# Generated by Django 2.1.1 on 2018-09-03 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('college_api', '0002_athleteemgdata_athletefeeditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='AthleteEMGDataItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emg_data', jsonfield.fields.JSONField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='athleteemgdata',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='AthleteEMGData',
        ),
    ]
