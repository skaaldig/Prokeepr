from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_update_relationships'),
    ]

    state_operations = [
        migrations.DeleteModel('Manufacturer'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
