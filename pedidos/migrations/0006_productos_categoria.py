# Generated by Django 5.1.6 on 2025-03-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_remove_pedido_mesa'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='categoria',
            field=models.IntegerField(choices=[(1, 'BEBIDAS CALIENTES'), (2, 'BEBIDAS FRÍAS'), (3, 'BOCADILLOS')], default='1'),
            preserve_default=False,
        ),
    ]
