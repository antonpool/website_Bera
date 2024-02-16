# Generated by Django 5.0.1 on 2024-02-16 07:56

import django.db.models.deletion
import mptt.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_alter_articles_slug_category_articles_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='подкатегория', to='news.category'),
        ),
    ]