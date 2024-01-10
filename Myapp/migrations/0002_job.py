# Generated by Django 4.2.7 on 2024-01-07 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('experience', models.PositiveIntegerField()),
                ('salary', models.PositiveIntegerField()),
                ('qualification', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('poster', models.ImageField(upload_to='poster')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Myapp.category')),
            ],
        ),
    ]
