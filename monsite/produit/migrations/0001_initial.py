# Generated by Django 3.1.4 on 2022-03-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article2',
            fields=[
                ('id_article', models.AutoField(primary_key=True, serialize=False)),
                ('code_famille', models.CharField(db_column='Code_famille', max_length=20)),
                ('cod_art', models.CharField(db_column='COD_ART', max_length=20)),
                ('des_art', models.CharField(blank=True, db_column='DES_ART', max_length=60, null=True)),
                ('cod_bar_fab', models.CharField(blank=True, db_column='COD_BAR_FAB', max_length=40, null=True)),
                ('cod_bar_int', models.CharField(blank=True, db_column='COD_BAR_INT', max_length=20, null=True)),
                ('taux_tva', models.CharField(max_length=10)),
                ('marge', models.CharField(max_length=10)),
                ('casier', models.CharField(blank=True, max_length=10, null=True)),
                ('unite', models.CharField(blank=True, max_length=10, null=True)),
                ('qte_stock', models.CharField(max_length=20)),
                ('qte_min', models.CharField(blank=True, max_length=10, null=True)),
                ('qte_max', models.CharField(blank=True, max_length=10, null=True)),
                ('reliquat', models.CharField(blank=True, db_column='Reliquat', max_length=10, null=True)),
                ('qte_initiale', models.CharField(max_length=20)),
                ('qte_promotion', models.CharField(blank=True, max_length=20, null=True)),
                ('qte_emballage_vente', models.CharField(blank=True, max_length=20, null=True)),
                ('qte_emballage_achat', models.CharField(max_length=20)),
                ('prix_achat_ht', models.CharField(max_length=20)),
                ('prix_vente_ht', models.CharField(max_length=20)),
                ('aprix_achat_ht', models.CharField(db_column='Aprix_achat_ht', max_length=20)),
                ('prix_vente_promotion', models.CharField(max_length=20)),
                ('a_prix_vente_ht', models.CharField(db_column='A_prix_vente_ht', max_length=20)),
                ('prix_vente_ttc', models.CharField(max_length=20)),
                ('prix_achat_ttc', models.CharField(max_length=20)),
                ('prix_achat_devise', models.CharField(max_length=20)),
                ('adaptable', models.CharField(blank=True, max_length=10, null=True)),
                ('equivalence', models.CharField(blank=True, max_length=20, null=True)),
                ('photo', models.CharField(blank=True, max_length=10, null=True)),
                ('deroi_consommation', models.CharField(blank=True, max_length=20, null=True)),
                ('article_compose', models.CharField(blank=True, max_length=20, null=True)),
                ('code_fournisseur', models.CharField(blank=True, max_length=20, null=True)),
                ('sans_code_abarre', models.CharField(blank=True, max_length=20, null=True)),
                ('avec_fodec', models.CharField(blank=True, max_length=10, null=True)),
                ('mode', models.CharField(blank=True, max_length=10, null=True)),
                ('complement_de_prix', models.CharField(max_length=20)),
                ('date_creation', models.CharField(blank=True, max_length=20, null=True)),
                ('qte_promotion_achat', models.CharField(blank=True, max_length=20, null=True)),
                ('prix_achat_promotion', models.CharField(max_length=20)),
                ('taux_vente', models.CharField(blank=True, max_length=10, null=True)),
                ('prix_achat_sansremise', models.CharField(max_length=30)),
                ('qte_initiale_anneepre', models.CharField(blank=True, max_length=30, null=True)),
                ('remise', models.CharField(max_length=10)),
                ('qte_encours', models.CharField(blank=True, max_length=20, null=True)),
                ('sans_stock', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.CharField(blank=True, max_length=20, null=True)),
                ('dernier_vente', models.CharField(blank=True, max_length=20, null=True)),
                ('dernier_achat', models.CharField(blank=True, max_length=20, null=True)),
                ('prix_achat_moyen', models.CharField(max_length=20)),
                ('aprix_achat_moyen', models.CharField(db_column='Aprix_achat_moyen', max_length=20)),
                ('color_article', models.CharField(blank=True, max_length=10, null=True)),
                ('poids', models.CharField(max_length=10)),
                ('unite_cart', models.CharField(blank=True, max_length=10, null=True)),
                ('categorie', models.CharField(blank=True, max_length=10, null=True)),
                ('marques', models.CharField(blank=True, max_length=10, null=True)),
                ('code_douane', models.CharField(blank=True, max_length=20, null=True)),
                ('remise_achat', models.CharField(max_length=20)),
                ('remise_vente', models.CharField(max_length=20)),
                ('prix_public', models.CharField(max_length=20)),
                ('ref_frs', models.CharField(blank=True, max_length=10, null=True)),
                ('remise_max', models.CharField(max_length=10)),
                ('prix_vente_min', models.CharField(max_length=20)),
                ('avec_fodec_achat', models.CharField(blank=True, max_length=20, null=True)),
                ('preferentiel', models.CharField(blank=True, max_length=20, null=True)),
                ('date_periem', models.CharField(blank=True, max_length=20, null=True)),
                ('pub_web', models.CharField(blank=True, max_length=10, null=True)),
                ('code_gfamille', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'article2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FamilleArticle',
            fields=[
                ('code_famille', models.IntegerField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=50)),
                ('id', models.IntegerField()),
                ('marge', models.IntegerField()),
                ('avec_fodec', models.CharField(max_length=50)),
                ('taux_tva', models.FloatField(db_column='taux_TVA')),
                ('ordre', models.IntegerField()),
                ('code_fournisseur', models.CharField(max_length=50)),
                ('aff_equi', models.CharField(max_length=50)),
                ('cod_art', models.CharField(max_length=50)),
                ('mp', models.CharField(db_column='MP', max_length=50)),
                ('pf', models.CharField(db_column='PF', max_length=50)),
                ('code_gfamille', models.CharField(max_length=50)),
                ('pub_web', models.IntegerField()),
            ],
            options={
                'db_table': 'famille_article',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GrandFamille',
            fields=[
                ('id_gfamille', models.IntegerField(primary_key=True, serialize=False)),
                ('designation', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=50)),
                ('pub_web', models.CharField(max_length=50)),
                ('date_modification', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'grand_famille',
                'managed': False,
            },
        ),
    ]
