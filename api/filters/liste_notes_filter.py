from django_filters import rest_framework as django_filters
from ..models import ListeNotes


class ListeNotesFilter(django_filters.FilterSet):
	# Filtering a range of notes
	note_min = django_filters.NumberFilter(field_name='note', lookup_expr='gte')
	note_max = django_filters.NumberFilter(field_name='note', lookup_expr='lte')

	class Meta:
		model = ListeNotes
		# Fields that can be filtered
		fields = ['matricule', 'mnemonique', 'note_min', 'note_max']