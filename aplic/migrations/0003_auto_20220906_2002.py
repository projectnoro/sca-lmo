# Generated by Django 2.2.19 on 2022-09-06 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_aluno_disciplina_professor_turma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='disciplina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplic.Disciplina'),
        ),
    ]
