# Generated by Django 4.2.5 on 2023-11-15 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0010_remove_person_city_remove_person_country_delete_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('districtname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchname', models.CharField(max_length=100)),
                ('distid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.district')),
            ],
        ),
    ]
