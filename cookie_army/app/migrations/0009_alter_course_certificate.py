# Generated by Django 4.0.8 on 2023-11-14 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_course_certificate_course_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Certificate',
            field=models.CharField(max_length=100, null=True),
        ),
    ]