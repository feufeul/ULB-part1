from rest_framework import serializers
from ..models import ListeCours


class ListeCoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeCours
        fields = '__all__'