from __future__ import unicode_literals

from django.db import migrations, models


def update_contentypes(apps, schema_editor):
    """
    Updates content types.
    We want to have the same content type id, when the model is moved and renamed.
    """
    ContentType = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias



def update_contentypes_reverse(apps, schema_editor):
    """
    Reverts changes in content types.
    """
    ContentType = apps.get_model('contenttypes', 'ContentType')
    db_alias = schema_editor.connection.alias


class Migration(migrations.Migration):

    dependencies = [
        # We need to run 0002_rename_table form app1 first,
        # because it changes the table of ModelThatShouldBeMoved.
        # Only after that we will update content types and rename the model.
        ('product', '0017_auto_20190506_0958'),
        # This migration also depends on the contenttype app,
        # so we need to specify dependency on 0002_remove_content_type_name.
        # If you use Django < 1.8, you will probably need to specify 0001_initial.
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
    ]

    database_operations = [
        migrations.RunPython(update_contentypes, update_contentypes_reverse),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=state_operations,
            database_operations=database_operations
        ),
    ]
