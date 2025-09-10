from rest_framework import viewsets
from ..models import ListeNotes
from ..serializers import ListeNotesSerializer
from ..filters.liste_notes_filter import ListeNotesFilter
from django_filters.rest_framework import DjangoFilterBackend


class ListeNotesViewSet(viewsets.ModelViewSet):
	queryset = ListeNotes.objects.all()
	serializer_class = ListeNotesSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_class = ListeNotesFilter