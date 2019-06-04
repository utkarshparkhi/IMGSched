# Generated by Django 2.2.2 on 2019-06-04 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitedEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('time', models.DateTimeField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Creator', to=settings.AUTH_USER_MODEL)),
                ('invitedUsers', models.ManyToManyField(related_name='usersinvited', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('time', 'title'),
            },
        ),
        migrations.CreateModel(
            name='GeneralEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('time', models.DateTimeField()),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=50)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('time', 'title'),
            },
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IMGsched.GeneralEvent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['pub_date'],
            },
        ),
    ]
