# Generated by Django 4.1.7 on 2023-04-01 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schnoogle_a', '0004_newsletter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='signup_date',
        ),
        migrations.AddField(
            model_name='feedback',
            name='message',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='subject',
            field=models.CharField(default='Newsletter Subscription', max_length=255),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]
