from rest_framework import viewsets
from ..models import ListeCours
from ..serializers import ListeCoursSerializer
from ..filters import ListeCoursFilter
from django_filters.rest_framework import DjangoFilterBackend


class ListeCoursViewSet(viewsets.ModelViewSet):
    queryset = ListeCours.objects.all()
    serializer_class = ListeCoursSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ListeCoursFilter