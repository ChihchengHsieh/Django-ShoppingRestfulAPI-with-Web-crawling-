# Generated by Django 2.2.2 on 2019-06-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderDate', models.DateTimeField(auto_now=True)),
                ('totalPrice', models.FloatField(default=0)),
                ('buyer', models.TextField(default='Unknow Buyer')),
                ('deliverDate', models.TextField(default='Unknown Date')),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
