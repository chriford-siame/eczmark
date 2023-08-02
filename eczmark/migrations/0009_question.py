# Generated by Django 3.2 on 2023-07-31 22:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eczmark', '0008_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('question_paper', models.FileField(null=True, upload_to='question-papers/-%H-%M-%S-%m/')),
                ('year_uncleaned', models.DateField(help_text='Enter any date containing the same year as the question paper selected.', null=True, verbose_name='Question paper year')),
                ('year_cleaned', models.CharField(blank=True, default='0000', max_length=4, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=4), django.core.validators.MaxLengthValidator(limit_value=4)])),
                ('grade', models.ForeignKey(help_text='Select the grade to which this question paper belong', null=True, on_delete=django.db.models.deletion.PROTECT, to='eczmark.grade', verbose_name='Grade')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eczmark.subject')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Marker')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
