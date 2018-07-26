# Generated by Django 2.0.2 on 2018-07-26 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFL_Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4)),
                ('fullName', models.CharField(max_length=100)),
                ('shortName', models.CharField(max_length=50)),
                ('byeWeek', models.IntegerField(default=-1)),
                ('sos', models.IntegerField(default=-1)),
                ('moneySOS', models.IntegerField(default=-1)),
                ('wk10', models.CharField(max_length=4)),
                ('wk11', models.CharField(max_length=4)),
                ('wk12', models.CharField(max_length=4)),
                ('wk13', models.CharField(max_length=4)),
                ('wk14', models.CharField(max_length=4)),
                ('wk15', models.CharField(max_length=4)),
                ('wk16', models.CharField(max_length=4)),
                ('qb_SOS', models.IntegerField(default=-1)),
                ('rb_SOS', models.IntegerField(default=-1)),
                ('wr_SOS', models.IntegerField(default=-1)),
                ('te_SOS', models.IntegerField(default=-1)),
            ],
        ),
    ]
