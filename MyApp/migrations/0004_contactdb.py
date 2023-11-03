# Generated by Django 4.2.5 on 2023-10-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_productdb_cname'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=20, null=True)),
                ('lastname', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
