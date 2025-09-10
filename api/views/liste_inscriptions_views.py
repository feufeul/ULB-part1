from rest_framework import viewsets
from ..models import ListeInscriptions
from ..serializers import ListeInscriptionsSerializer

class ListeInscriptionsViewSet(viewsets.ModelViewSet):
    queryset = ListeInscriptions.objects.all()
    serializer_class = ListeInscriptionsSerializer
