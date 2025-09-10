# ULB Part1 - API Django

Projet de démonstration d'API Django REST exposant des données à partir d'une base SQLite existante.

## Installation rapide

1. **Cloner le projet**
   
   git clone https://github.com/feufeul/part1.git
   cd part1

2. **Créer et activer un environnement virtuel**
	
	python3 -m venv myenv
	source myenv/bin/activate

3. **Installer les dépendances**

	pip install -r requirements.txt

4. **Configurer la base de données**

	Placer le fichier SQLite fourni à la racine du projet (ou adaptez le chemin dans settings.py)
	python manage.py makegrations
	python manage.py migrate

5. **Lancer le serveur de développement**

	python manage.py runserver

6. **Tester l'API**

	Accédez à http://127.0.0.1:8000/api/ avec les endpoints suivants:
	* /liste_cours/
	* /liste_inscriptions/
	* /liste_notes/

## Dépendances principales

	Django, djangorestframework, django-filter

## Contact

	Pour toute question, contactez vanduffelchristopher@gmail.com