
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0012_auto_20191126_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo2',
            field=models.CharField(max_length=100, null=True),
        ), 
    ]
