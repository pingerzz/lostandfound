<<<<<<< HEAD
# Generated by Django 5.1.5 on 2025-01-16 11:01
=======
<<<<<<< HEAD
# Generated by Django 5.1.5 on 2025-01-16 11:01
=======
# Generated by Django 5.1.4 on 2025-01-04 15:05
>>>>>>> 99fd0ab869c0cdfd9b146f3a3b0f1108d21af5d3
>>>>>>> 747490cf7a9693f695fb9a8700a8c73271d7b9b7

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 747490cf7a9693f695fb9a8700a8c73271d7b9b7
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the category (e.g., Electronics, Clothing, Accessories).', max_length=100, unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional detailed description of the category.', null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LostAndFoundItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(help_text="A short title describing the item (e.g., 'Lost Wallet').", max_length=100)),
                ('description', models.TextField(help_text='Detailed description of the item.')),
                ('status', models.CharField(choices=[('lost', 'Lost'), ('found', 'Found')], help_text='Is this item lost or found?', max_length=10)),
                ('location', models.CharField(help_text='Where was the item lost or found?', max_length=255)),
                ('date', models.DateField(help_text='Date when the item was lost or found.')),
                ('contact_name', models.CharField(help_text='Name of the contact person.', max_length=100)),
                ('contact_phone', models.CharField(blank=True, help_text='Optional phone number for contacting.', max_length=15, null=True)),
                ('image', models.ImageField(blank=True, help_text='Optional image of the item.', null=True, upload_to='lost_and_found_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Lost and Found Item',
                'verbose_name_plural': 'Lost and Found Items',
                'ordering': ['-date'],
            },
<<<<<<< HEAD
=======
=======
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('desc', models.TextField(blank=True, max_length=250)),
            ],
>>>>>>> 99fd0ab869c0cdfd9b146f3a3b0f1108d21af5d3
>>>>>>> 747490cf7a9693f695fb9a8700a8c73271d7b9b7
        ),
    ]
