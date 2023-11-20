import django_filters
from .models import User

class UsertFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = User
        fields = ['username']