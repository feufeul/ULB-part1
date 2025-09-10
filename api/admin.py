from django.contrib import admin
from .models import ListeInscriptions, ListeCours, ListeNotes

# Register your models here.
for model in [ListeInscriptions, ListeCours, ListeNotes]:
	admin.site.register(model)