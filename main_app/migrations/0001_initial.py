# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-04 13:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthAppShopUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('myshopify_domain', models.CharField(editable=False, max_length=255, unique=True)),
                ('token', models.CharField(default=b'00000000000000000000000000000000', editable=False, max_length=32)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubscriptionLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_level_name', models.CharField(max_length=64, unique=True)),
                ('charge_description', models.CharField(blank=True, max_length=255, null=True)),
                ('charge_terms', models.CharField(blank=True, max_length=255, null=True)),
                ('trial_days', models.IntegerField(default=14)),
                ('subscription_price', models.FloatField(default=20.99)),
                ('test_flag', models.BooleanField(default=False)),
                ('subscription_slug', models.SlugField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TermsAndConditionText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_terms', models.TextField(default=b'Terms text content')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_timezone', models.CharField(max_length=128)),
                ('iana_timezone', models.CharField(max_length=128)),
                ('latest_product_sync_time', models.DateTimeField(blank=True, null=True)),
                ('marketing_first_name', models.CharField(blank=True, max_length=128, null=True)),
                ('marketing_last_name', models.CharField(blank=True, max_length=128, null=True)),
                ('marketing_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('shop_customer_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('shop_contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('accepts_marketing_emails', models.BooleanField(default=False)),
                ('accepts_status_emails', models.BooleanField(default=False)),
                ('setup_required', models.BooleanField(default=True)),
                ('terms_and_conditions_consent', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.Session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_id', models.BigIntegerField(blank=True, null=True)),
                ('charge_status', models.CharField(blank=True, max_length=64, null=True)),
                ('subscription_level', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='main_app.SubscriptionLevel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
