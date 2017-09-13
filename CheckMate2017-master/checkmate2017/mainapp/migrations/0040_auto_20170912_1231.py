# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-12 12:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0039_userprofile_bstat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='idno1',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(re.compile(b'^201[0-9]{1}[0-9A-Z]{4}[0-9]{4}P$'), code=b'invalid!', message=b'Enter your valid BITS-mail')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='idno2',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(re.compile(b'^201[0-9]{1}[0-9A-Z]{4}[0-9]{4}P$'), code=b'invalid!', message=b'Enter your valid BITS-mail')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sprite',
            field=models.CharField(choices=[(b'girl', b'girl'), (b'boy', b'boy')], default=b'Null', max_length=50),
        ),
    ]