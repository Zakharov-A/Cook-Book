# Generated by Django 5.1.3 on 2024-11-30 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipes_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
