# Generated by Django 4.2.5 on 2023-09-29 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(blank=True, max_length=20, null=True)),
                ('des', models.CharField(blank=True, max_length=50, null=True)),
                ('pri', models.IntegerField(blank=True, null=True)),
                ('pimg', models.ImageField(blank=True, null=True, upload_to='product_img')),
            ],
        ),
    ]
