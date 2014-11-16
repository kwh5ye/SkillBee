# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=3, choices=[(b'APP', b'Web and Mobile Apps'), (b'SUP', b'Tech Support'), (b'SOC', b'Social Media')])),
                ('progress', models.CharField(default=b'NA', max_length=2, choices=[(b'NA', b'Not accepted'), (b'IP', b'In progress'), (b'CP', b'Completed')])),
                ('student_id', models.IntegerField()),
                ('client_id', models.IntegerField()),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
