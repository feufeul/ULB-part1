from django.db import models

class ListeNotes(models.Model):
	# Auto-generated primary key field 'id' will be created by default
	id = models.AutoField(primary_key=True)
	matricule = models.TextField()
	mnemonique = models.TextField()
	note = models.FloatField()

	class Meta:
		db_table = 'liste_notes'