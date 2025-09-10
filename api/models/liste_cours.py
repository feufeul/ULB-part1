from django.db import models

class ListeCours(models.Model):
	mnemonique = models.TextField(primary_key=True)
	intitule = models.TextField()
	credit = models.IntegerField()
	titulaire = models.TextField()

	class Meta:
		db_table = 'liste_cours'