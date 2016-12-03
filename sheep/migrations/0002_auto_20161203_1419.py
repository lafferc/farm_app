# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sheep.models


class Migration(migrations.Migration):

    dependencies = [
        ('sheep', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sheep',
            options={'verbose_name_plural': 'Sheep'},
        ),
        migrations.AlterField(
            model_name='lambingyear',
            name='year',
            field=models.IntegerField(default=sheep.models.current_year, choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)]),
        ),
        migrations.AlterField(
            model_name='sheep',
            name='yob',
            field=models.IntegerField(blank=True, null=True, choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)]),
        ),
    ]
