# Generated by Django 3.1.3 on 2021-07-31 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='listing',
            name='file_path',
            field=models.ImageField(blank=True, null=True, upload_to='imgaes/', verbose_name=''),
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='auctions.category'),
        ),
    ]