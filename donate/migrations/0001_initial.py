# Generated by Django 4.0.1 on 2022-03-07 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('payment_id', models.CharField(max_length=100)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
    ]
