# Generated by Django 3.1.2 on 2020-12-21 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_showing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=11)),
            ],
        ),
        migrations.AlterModelOptions(
            name='showing',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='showing',
            name='date',
            field=models.DateField(verbose_name='showing date'),
        ),
        migrations.AddField(
            model_name='property',
            name='buyers',
            field=models.ManyToManyField(to='main_app.Buyer'),
        ),
    ]
