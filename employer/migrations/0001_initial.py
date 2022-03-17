# Generated by Django 3.2.11 on 2022-03-15 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=120)),
                ('services', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('User', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=50)),
                ('experience', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=150)),
                ('posted_date', models.DateField(auto_now_add=True, null=True)),
                ('last_date', models.DateField()),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employer.companyprofile')),
            ],
        ),
    ]