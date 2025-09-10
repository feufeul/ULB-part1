from django.db import models

class ListeInscriptions(models.Model):
	matricule = models.TextField(primary_key=True)
	nom = models.TextField()
	prenom = models.TextField()
	annee_etude = models.IntegerField()
	cours_json = models.TextField()

	class Meta:
		db_table = 'liste_inscriptions'