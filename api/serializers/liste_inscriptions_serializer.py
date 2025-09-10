from rest_framework import serializers
from ..models import ListeInscriptions
import json


class ListeInscriptionsSerializer(serializers.ModelSerializer):
	cours = serializers.SerializerMethodField()
	
	class Meta:
		model = ListeInscriptions
		fields = ['matricule', 'nom', 'prenom', 'annee_etude', 'cours']
	
	# Method to parse the JSON field into a Python list
	def get_cours(self, obj):
		try:
			return json.loads(obj.cours_json) if obj.cours_json else []
		except json.JSONDecodeError:
			return []