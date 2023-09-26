# Generated by Django 4.0.3 on 2023-04-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('court_system', '0002_cases_instances_courts_remove_case_charge_sheet_ptr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lawyers',
            name='name',
        ),
        migrations.AddField(
            model_name='advocates_roll_number',
            name='name',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
    ]
