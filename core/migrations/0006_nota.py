# Generated by Django 5.2.2 on 2025-06-25 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_merge_20250625_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
                ('data_lancamento', models.DateField()),
                ('observacao', models.CharField(blank=True, max_length=255)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='core.aluno')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notas', to='core.disciplina')),
            ],
        ),
    ]
