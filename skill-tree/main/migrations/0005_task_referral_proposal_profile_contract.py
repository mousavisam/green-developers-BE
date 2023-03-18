# Generated by Django 4.1.6 on 2023-03-14 19:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import main.shared.utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_category_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('deliver_time', models.DateField()),
                ('status', models.CharField(choices=[('ASSIGNED', 'Assigned'), ('UNASSIGNED', 'Unassigned'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')], max_length=20)),
                ('description', models.TextField()),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('service_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now=True)),
                ('referee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='referee', to=settings.AUTH_USER_MODEL)),
                ('referer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='referer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_time_in_day', models.PositiveIntegerField()),
                ('payment_amount', models.DecimalField(decimal_places=3, max_digits=12)),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('REJECT', 'Reject'), ('ACCEPT', 'Accept')], max_length=20)),
                ('description', models.TextField()),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.task')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('count_of_served_tasks', models.IntegerField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('count_of_requested_tasks', models.IntegerField(validators=[django.core.validators.MinValueValidator(0.0)])),
                ('joined_date', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('BUSY', 'Busy'), ('FREE', 'Free')], max_length=20)),
                ('personal_image', models.ImageField(upload_to=main.shared.utils.SkillTreeUtils.get_profile_user_file_path)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved')], max_length=20)),
                ('delivery_time_in_day', models.PositiveIntegerField()),
                ('payment_amount', models.DecimalField(decimal_places=3, max_digits=12)),
                ('payment_type', models.CharField(choices=[('PER_HOUR', 'Per Hour'), ('AFTER_DONE', 'After Done'), ('AFTER_SPECIFIC_PART', 'After Specific Part')], max_length=20)),
                ('creation_time', models.DateTimeField(auto_now=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('proposal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.proposal')),
            ],
        ),
    ]
