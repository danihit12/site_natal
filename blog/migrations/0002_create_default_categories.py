from django.db import migrations


def create_default_categories(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')
    for name in ["decoração", "família", "comidas"]:
        Category.objects.get_or_create(name=name)


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories),
    ]
