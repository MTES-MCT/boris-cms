# Generated by Django 5.0.8 on 2024-09-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0033_alter_blogentrypage_body_alter_blogindexpage_body"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="sort_order",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="sort_order",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="person",
            name="sort_order",
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]