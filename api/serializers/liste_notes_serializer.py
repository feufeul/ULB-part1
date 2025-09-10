from rest_framework import serializers
from ..models import ListeNotes


class ListeNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeNotes
        fields = '__all__'
