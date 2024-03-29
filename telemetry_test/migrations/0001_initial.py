# Generated by Django 2.2.7 on 2019-11-21 15:26

from django.db import migrations, models
import django.db.models.manager
import telemetry_test.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=30)),
                ('description_type', models.CharField(max_length=100)),
                ('file_extension', models.CharField(max_length=10)),
                ('file_size', models.IntegerField()),
                ('folder_path', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Document Type',
                'verbose_name_plural': 'Document Types',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_id', models.IntegerField(verbose_name='id_element')),
                ('from_model', models.CharField(max_length=20)),
                ('element_id_from_model', models.CharField(max_length=20)),
                ('attachment_file', models.FileField(upload_to=telemetry_test.models.directory_path, verbose_name='File')),
                ('file_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='File name')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(editable=False, on_delete='DO_NOTHING', to='telemetry_test.Company')),
                ('document_type', models.ForeignKey(on_delete='DO_NOTHING', to='telemetry_test.DocumentType')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
