# Generated by Django 4.1.2 on 2022-10-31 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment_text'),
        ('accounts', '0007_remove_account_liked_posts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='liked_posts',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_likes', to='posts.post', verbose_name='Понравившиеся публикации'),
        ),
    ]
