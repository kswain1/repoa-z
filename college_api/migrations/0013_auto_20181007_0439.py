# Generated by Django 2.1.1 on 2018-10-07 04:39

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('college_api', '0012_auto_20181006_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='peroneals_rle',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
    ]
