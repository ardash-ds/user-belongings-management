# Generated by Django 4.1.3 on 2022-11-29 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('obj_card', '0005_remove_picture_obj_object_pictures_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='category',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='obj_card.category'),
            preserve_default=False,
        ),
    ]
