# Generated by Django 5.0.6 on 2024-07-15 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Elections',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('cutoff_time', models.TimeField()),
                ('status', models.CharField(choices=[('Incoming', 'Imcoming'), ('Open', 'Open'), ('Closed', 'Closed')], default='Incomming', max_length=50)),
                ('is_deleted', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('position_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_deleted', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nominations',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('election', models.ForeignKey(db_column='election_id', on_delete=django.db.models.deletion.CASCADE, to='board.elections')),
                ('member', models.ForeignKey(db_column='member_id', on_delete=django.db.models.deletion.CASCADE, to='members.memreg')),
                ('position', models.ForeignKey(db_column='position_id', on_delete=django.db.models.deletion.CASCADE, to='board.positions')),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('qr_code', models.ImageField(blank=True, null=True, upload_to='qr_codes/')),
                ('is_deleted', models.BooleanField(default=True)),
                ('nomination', models.ForeignKey(db_column='nomination_id', on_delete=django.db.models.deletion.CASCADE, to='board.nominations')),
            ],
        ),
    ]