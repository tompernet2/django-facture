# Generated by Django 5.2.3 on 2025-06-18 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_alter_produit_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture',
            name='produits',
        ),
        migrations.CreateModel(
            name='LigneFacture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_peremption', models.DateField()),
                ('facture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lignes', to='gestion.facture')),
            ],
        ),
    ]
