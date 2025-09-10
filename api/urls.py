from rest_framework import routers
from .views import ListeNotesViewSet, ListeCoursViewSet, ListeInscriptionsViewSet

router = routers.DefaultRouter()

router.register(r'liste_notes', ListeNotesViewSet)
router.register(r'liste_cours', ListeCoursViewSet)
router.register(r'liste_inscriptions', ListeInscriptionsViewSet)

urlpatterns = router.urls