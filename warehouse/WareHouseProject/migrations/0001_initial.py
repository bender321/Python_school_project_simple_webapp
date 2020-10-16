# Generated by Django 2.1.3 on 2018-11-18 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('customer_of_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseProject.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=250)),
                ('stock_cost', models.CharField(max_length=10)),
                ('stock_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WareHouseProject.Company')),
            ],
        ),
    ]
