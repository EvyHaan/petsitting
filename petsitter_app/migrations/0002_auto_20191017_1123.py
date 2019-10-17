# Generated by Django 2.2.6 on 2019-10-17 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsitter_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/family'),
        ),
        migrations.AlterField(
            model_name='family',
            name='contact2',
            field=models.CharField(blank=True, max_length=48),
        ),
        migrations.AlterField(
            model_name='family',
            name='contact2_email',
            field=models.CharField(blank=True, max_length=48),
        ),
        migrations.AlterField(
            model_name='family',
            name='contact2_phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='family',
            name='emergency1_contact',
            field=models.CharField(blank=True, max_length=48),
        ),
        migrations.AlterField(
            model_name='family',
            name='emergency1_phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='family',
            name='emergency2_contact',
            field=models.CharField(blank=True, max_length=48),
        ),
        migrations.AlterField(
            model_name='family',
            name='emergency2_phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='family',
            name='notes',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='family',
            name='vet',
            field=models.CharField(blank=True, max_length=48),
        ),
        migrations.AlterField(
            model_name='family',
            name='vet_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='family',
            name='vet_phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='bio',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='pet',
            name='daily_routine',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='pet',
            name='feeding_routine',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='pet',
            name='medical_routine',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='pet',
            name='other_notes',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/pets'),
        ),
    ]