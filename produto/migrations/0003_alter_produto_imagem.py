# Generated by Django 4.2.6 on 2023-10-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_rename_produtos_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='produto_imagens/%Y/%m/'),
        ),
    ]
