# Generated by Django 4.1.1 on 2022-11-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0004_delete_imagens_alter_cliente_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='login',
        ),
        migrations.AddField(
            model_name='cliente',
            name='password',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]