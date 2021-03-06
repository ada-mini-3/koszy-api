# Generated by Django 3.0.8 on 2020-07-19 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200719_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussionimage',
            name='discussion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussion_image', to='core.CommunityDiscussion'),
        ),
        migrations.AlterField(
            model_name='feedimage',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_feed', to='core.Feed'),
        ),
    ]
