# Generated by Django 2.0.3 on 2018-03-28 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20180328_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='miremotecommand',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='miremotecommand',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
