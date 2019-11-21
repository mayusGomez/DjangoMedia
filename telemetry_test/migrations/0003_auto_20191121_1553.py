# Generated by Django 2.2.7 on 2019-11-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telemetry_test', '0002_telemetrytest'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='folder_params',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='documenttype',
            name='sub_folder_path',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='company',
            field=models.ForeignKey(on_delete='DO_NOTHING', to='telemetry_test.Company'),
        ),
        migrations.AlterField(
            model_name='documenttype',
            name='folder_path',
            field=models.CharField(max_length=10),
        ),
    ]
