# Generated by Django 4.1.3 on 2023-05-13 14:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_students_alter_user_teachers'),
    ]

    operations = [
        migrations.CreateModel(
            name='habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=450)),
                ('img', models.ImageField(upload_to='habilidades')),
                ('pontuacao', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=1000)),
                ('percent', models.IntegerField(default=0, help_text='Porcetagem da habilidades')),
                ('user', models.ManyToManyField(blank=True, related_name='habilidades', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Habilidade',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.IntegerField(default=0)),
                ('percent', models.IntegerField(default=0, help_text='Porcetagem da Experiência')),
                ('pontuacao', models.IntegerField(default=0, help_text='Pontuação da Experiência')),
                ('total', models.IntegerField(default=0, help_text='total da Experiência do nivel')),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.ManyToManyField(blank=True, related_name='experiências', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Experiência',
                'verbose_name_plural': 'Experiências',
            },
        ),
    ]
