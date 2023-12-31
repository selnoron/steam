# Generated by Django 4.2.3 on 2023-07-29 18:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0010_alter_invitecard_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitecard',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 29, 0, 35, 0, 421970), verbose_name='дата истечения'),
        ),
        migrations.CreateModel(
            name='ImagesDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screens', models.ImageField(default='games/unknown.png', upload_to='games/', verbose_name='изображение')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images_of_games', to='games.game', verbose_name='игра')),
            ],
        ),
    ]
