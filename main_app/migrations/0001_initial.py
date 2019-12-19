# Generated by Django 2.2.6 on 2019-12-19 00:05

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
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('label', models.CharField(max_length=100)),
                ('condition', models.CharField(choices=[('M', 'Mint'), ('E', 'Excellent'), ('VG+', 'Very Good Plus'), ('VG', 'Very Good'), ('G', 'Good'), ('F', 'Fair'), ('P', 'Poor')], default='G', max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]