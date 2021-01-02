# Generated by Django 3.1.4 on 2021-01-02 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_auto_20210101_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='birthday',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='coach',
            name='info',
            field=models.TextField(default='这里空荡荡的，什么也没有。'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='tel',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='isvip',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='普通用户', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='regtime',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tel',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='vipend',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='vipstart',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('star', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.user')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('msg', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym.user')),
            ],
        ),
    ]
