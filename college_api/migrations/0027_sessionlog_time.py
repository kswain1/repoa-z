# Generated by Django 2.1.1 on 2018-12-20 19:01

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('college_api', '0026_sessionlog_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessionlog',
            name='time',
            field=jsonfield.fields.JSONField(blank=True, null=-1),
            preserve_default=-1,
        ),
    ]