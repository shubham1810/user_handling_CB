# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20161022_0713'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assignment_name', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=500)),
                ('max_score', models.IntegerField(default=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_link', models.CharField(max_length=200, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=0)),
                ('assignment', models.ForeignKey(to='main.Assignment')),
                ('user', models.ForeignKey(to='main.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='score',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='institution',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
    ]
