# Generated by Django 4.2.16 on 2024-11-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "myapp",
            "0004_rename_water_density_waterresourcemanagement_water_intensity_and_more",
        ),
    ]

    operations = [
        migrations.RenameField(
            model_name="energymanagement",
            old_name="renewable_energy_usage_rate",
            new_name="usage_rate",
        ),
        migrations.AddField(
            model_name="energymanagement",
            name="market",
            field=models.CharField(
                default="default_value_here", max_length=50, verbose_name="市場別"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="energymanagement",
            name="certification",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="取得驗證"
            ),
        ),
        migrations.AlterField(
            model_name="energymanagement",
            name="company_code",
            field=models.CharField(max_length=20, verbose_name="公司代號"),
        ),
        migrations.AlterField(
            model_name="energymanagement",
            name="company_name",
            field=models.CharField(max_length=100, verbose_name="公司名稱"),
        ),
    ]
