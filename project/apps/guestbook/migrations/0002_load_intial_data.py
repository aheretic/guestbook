# coding: utf-8
from __future__ import unicode_literals
import os

from django.db import migrations
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    call_command("loaddata", "initial_data.json", app_label="guestbook")


def unload_fixture(apps, schema_editor):
    apps.get_model("guestbook", "CustomUser").objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("guestbook", "0001_initial"),
    ]
    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]