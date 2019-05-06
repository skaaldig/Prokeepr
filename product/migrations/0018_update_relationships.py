from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        # The previous migration in app1
        ('product', '0017_auto_20190506_0958'),
        # This migration should depend on the migration that creates a model in the state of app2,
        # because we are going to refer a new model here.
        ('manufacturer', '0001_move_manufacturer_and_rename'),
    ]

    state_operations = [
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    to='manufacturer.Manufacturer'),
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
