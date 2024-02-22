# Generated by Django 5.0.1 on 2024-02-15 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=1000)),
                ('completed', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, default=1, max_length=10, null=True)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.person')),
            ],
        ),
    ]