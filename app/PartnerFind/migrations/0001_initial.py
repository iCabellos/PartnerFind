# Generated by Django 4.2.6 on 2023-11-08 13:00

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchModel',
            fields=[
                ('match_id', models.AutoField(primary_key=True, serialize=False)),
                ('match_name', models.CharField(help_text='Selecciona el nombre de la partida', max_length=50)),
            ],
            options={
                'ordering': ['-match_name'],
            },
        ),
        migrations.CreateModel(
            name='UserGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('user_email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('groups', models.ManyToManyField(related_name='custom_user_groups', through='PartnerFind.UserGroups', to='auth.group')),
            ],
            options={
                'db_table': 'custom_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserUserPermissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PartnerFind.usermodel')),
            ],
        ),
        migrations.AddField(
            model_name='usermodel',
            name='user_permissions',
            field=models.ManyToManyField(related_name='custom_user_permissions', through='PartnerFind.UserUserPermissions', to='auth.permission'),
        ),
        migrations.AddField(
            model_name='usergroups',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PartnerFind.usermodel'),
        ),
        migrations.CreateModel(
            name='MatchPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PartnerFind.matchmodel')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PartnerFind.usermodel')),
            ],
            options={
                'unique_together': {('match', 'player')},
            },
        ),
        migrations.AddField(
            model_name='matchmodel',
            name='players',
            field=models.ManyToManyField(related_name='matches', through='PartnerFind.MatchPlayer', to='PartnerFind.usermodel'),
        ),
    ]