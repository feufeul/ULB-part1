from ..models import ListeInscriptions
from django_filters import rest_framework as django_filters


class ListeInscriptionsFilter(django_filters.FilterSet):
	class Meta:
		model = ListeInscriptions
		fields = ['matricule', 'nom', 'prenom', 'annee_etude']