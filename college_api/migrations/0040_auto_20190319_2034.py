# Generated by Django 2.1.1 on 2019-03-19 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_api', '0039_auto_20190315_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompositeScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leg_length_rle', models.FloatField(blank=True, default=0.0, null=True)),
                ('leg_length_lle', models.FloatField(blank=True, default=0.0, null=True)),
                ('anterior_rle', models.FloatField(blank=True, default=0.0, null=True)),
                ('anterior_lle', models.FloatField(blank=True, default=0.0, null=True)),
                ('posterior_medial_rle', models.FloatField(blank=True, default=0.0, null=True)),
                ('posterior_medial_lle', models.FloatField(blank=True, default=0.0, null=True)),
                ('posterior_lateral_rle', models.FloatField(blank=True, default=0.0, null=True)),
                ('posterior_lateral_lle', models.FloatField(blank=True, default=0.0, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college_api.Player')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='anterior_lle',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='anterior_rle',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='composite_score_lle',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='composite_score_rle',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='leg_length_lle',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='leg_length_rle',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='posterior_lateral_lle',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='posterior_lateral_rle',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='posterior_medial_lle',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='playerprofile',
            name='posterior_medial_rle',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
