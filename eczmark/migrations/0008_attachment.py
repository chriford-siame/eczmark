# Generated by Django 3.2 on 2023-07-31 22:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eczmark', '0007_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('file', models.ImageField(upload_to='attachments/%Y-%M-%d/')),
                ('note', models.CharField(blank=True, help_text='A quick note about this supporting image. Must have words between 20 and 100.', max_length=100, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=15), django.core.validators.MaxLengthValidator(limit_value=100)], verbose_name='Note')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
