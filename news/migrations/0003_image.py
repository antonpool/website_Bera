# Generated by Django 4.2.8 on 2024-01-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_resume_alter_articles_options_alter_articles_anons_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(max_length=255, null=True, upload_to='images/')),
            ],
        ),
    ]
