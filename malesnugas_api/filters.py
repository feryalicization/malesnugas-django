import django_filters
from .models import User

class UsertFilter(django_filters.FilterSet):
    # username = django_filters.CharFilter(lookup_expr='iexact')
    username = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['username']