# Generated by Django 2.2 on 2019-11-05 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
            ],
            options={
                'ordering': ('name', 'manufacturer'),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
