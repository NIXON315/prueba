from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0013_auto_20191126_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opciones',
            name='moneda',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
