# Generated by Django 3.0.3 on 2020-02-25 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import profiles.models.profilePicture
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilePicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(upload_to=profiles.models.profilePicture.profile_picture_attachment_path)),
                ('thumbnail', models.ImageField(upload_to=profiles.models.profilePicture.profile_picture_thumbnail_attachment_path)),
                ('priority', models.IntegerField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_pictures', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]