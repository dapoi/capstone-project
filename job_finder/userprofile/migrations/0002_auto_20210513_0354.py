# Generated by Django 3.2.2 on 2021-05-12 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('datafile', models.FileField(upload_to='')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image_company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/company', verbose_name='Image')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
                ('company', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.company')),
            ],
        ),
        migrations.CreateModel(
            name='Image_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/user', verbose_name='Image')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_cv',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='user_pdf',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='user_pic',
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='user_cv',
        ),
    ]