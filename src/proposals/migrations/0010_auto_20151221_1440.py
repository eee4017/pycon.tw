# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-21 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0009_auto_20151221_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talkproposal',
            name='category',
            field=models.CharField(choices=[('PRAC', 'Best Practices & Patterns'), ('COM', 'Community'), ('DB', 'Databases'), ('DATA', 'Data Analysis'), ('EDU', 'Education'), ('EMBED', 'Embedded Systems'), ('GAME', 'Gaming'), ('GRAPH', 'Graphics'), ('OTHER', 'Other'), ('CORE', 'Python Core (language, stdlib, etc.)'), ('INTNL', 'Python Internals'), ('LIBS', 'Python Libraries'), ('SCI', 'Science'), ('SEC', 'Security'), ('ADMIN', 'Systems Administration'), ('TEST', 'Testing'), ('WEB', 'Web Frameworks')], max_length=5, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='tutorialproposal',
            name='category',
            field=models.CharField(choices=[('PRAC', 'Best Practices & Patterns'), ('COM', 'Community'), ('DB', 'Databases'), ('DATA', 'Data Analysis'), ('EDU', 'Education'), ('EMBED', 'Embedded Systems'), ('GAME', 'Gaming'), ('GRAPH', 'Graphics'), ('OTHER', 'Other'), ('CORE', 'Python Core (language, stdlib, etc.)'), ('INTNL', 'Python Internals'), ('LIBS', 'Python Libraries'), ('SCI', 'Science'), ('SEC', 'Security'), ('ADMIN', 'Systems Administration'), ('TEST', 'Testing'), ('WEB', 'Web Frameworks')], max_length=5, verbose_name='category'),
        ),
    ]
