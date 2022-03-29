# Generated by Django 4.0.3 on 2022-03-07 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_clothingtype_company_companymodel_size_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothingtype',
            name='points',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='companymodel',
            name='dimensions',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='dimensions',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='clothingtype',
            name='label',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='adress',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='companymodel',
            name='color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='size',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='size',
            name='label',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='size',
            name='origin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]