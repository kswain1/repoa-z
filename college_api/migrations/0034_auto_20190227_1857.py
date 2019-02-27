# Generated by Django 2.1.1 on 2019-02-27 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college_api', '0033_auto_20190226_0157'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_role', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='mvclog',
            old_name='user_profile',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='mvclog',
            name='mvc',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='college_api.MVCType'),
            preserve_default=False,
        ),
    ]