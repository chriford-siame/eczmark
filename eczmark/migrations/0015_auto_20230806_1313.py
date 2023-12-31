# Generated by Django 3.2 on 2023-08-06 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eczmark', '0014_refactor_field_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='year_cleaned',
            new_name='cleaned_year',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(blank=True, help_text='Select the question to be answered', null=True, on_delete=django.db.models.deletion.CASCADE, to='eczmark.question', verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='attachments',
            field=models.ManyToManyField(blank=True, to='eczmark.Attachment', verbose_name='Supporting images'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='links',
            field=models.ManyToManyField(blank=True, to='eczmark.Link', verbose_name='Supporting link'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Question Poster Name'),
        ),
    ]
