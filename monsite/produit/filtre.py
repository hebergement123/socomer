
import django_filters

from .models import Article2, Temp,Commande
class ArticleFiltre(django_filters.FilterSet):

    #name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Article2
        fields = ['code_famille', 'des_art','cod_art','oem','equivalence']

class CommandeFiltre(django_filters.FilterSet):
    class Meta:
        model = Commande
        fields = ['date']