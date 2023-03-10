# Generated by Django 3.2.9 on 2022-09-10 12:17
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NFT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rarity_score', models.FloatField(null=True)),
                ('nft_id', models.PositiveIntegerField()),
                ('image_url', models.CharField(max_length=200)),
                ('rank', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NFTAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NFTProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_address', models.CharField(max_length=100)),
                ('contract_abi', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('number_of_nfts', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NFTTrait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rarity_score', models.FloatField(null=True)),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traits', to='nft.nftattribute')),
                ('nft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nft_attributes', to='nft.nft')),
            ],
        ),
        migrations.AddField(
            model_name='nftattribute',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attributes', to='nft.nftproject'),
        ),
        migrations.AddField(
            model_name='nft',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nfts', to='nft.nftproject'),
        ),
    ]
