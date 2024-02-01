# Generated by Django 4.2.6 on 2024-01-30 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('username', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('address', models.TextField()),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.registration')),
            ],
        ),
    ]
