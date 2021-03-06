# Generated by Django 3.2.12 on 2022-03-27 23:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('customer_name', models.CharField(blank=True, max_length=200, null=True)),
                ('meal_type', models.CharField(blank=True, max_length=300, null=True)),
                ('meal_price', models.FloatField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
