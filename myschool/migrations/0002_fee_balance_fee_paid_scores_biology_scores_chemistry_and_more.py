# Generated by Django 4.0.3 on 2022-04-21 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='balance',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fee',
            name='paid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scores',
            name='biology',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scores',
            name='chemistry',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scores',
            name='english',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scores',
            name='kiswahili',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scores',
            name='mathematics',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scores',
            name='physics',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scores',
            name='term',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scores',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='f_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='form',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='l_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='parent_name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='parent_phone',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='adm_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject1',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject2',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='tsc_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
