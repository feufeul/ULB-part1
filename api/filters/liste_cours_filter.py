from ..models import ListeCours
from django_filters import rest_framework as django_filters


class ListeCoursFilter(django_filters.FilterSet):
	# Filtering a range of credits
	credit_min = django_filters.NumberFilter(field_name='credit', lookup_expr='gte')
	credit_max = django_filters.NumberFilter(field_name='credit', lookup_expr='lte')

	class Meta:
		model = ListeCours
		fields = ['mnemonique', 'intitule', 'credit', 'titulaire']