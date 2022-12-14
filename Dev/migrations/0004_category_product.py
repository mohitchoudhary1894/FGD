# Generated by Django 4.0.6 on 2022-09-14 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dev', '0003_rename_password_name_registration_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(max_length=300)),
                ('pro_image', models.ImageField(upload_to='upload/')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dev.category')),
            ],
        ),
    ]
