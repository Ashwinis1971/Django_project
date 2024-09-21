# Generated by Django 5.0.7 on 2024-08-30 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app2', '0003_censorinfo_movieinfo_cursor_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieinfo',
            name='directed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='directed_movie', to='movies_app2.director'),
        ),
    ]