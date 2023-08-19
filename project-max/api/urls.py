from rest_framework import routers
from .api import OwnerViewSet,EspecieViewSet,RazaViewSet,petSizeViewSet,PetsViewSet,VacunaViewSet,citaMedicaViewSet
router = routers.DefaultRouter()

router.register('api/owner', OwnerViewSet, 'owner')
router.register('api/especie', EspecieViewSet,'especie')
router.register('api/raza',RazaViewSet,'raza')
router.register('api/petSize',petSizeViewSet,'petSize')
router.register('api/pets',PetsViewSet,'pets')
router.register('api/vacuna',VacunaViewSet,'vacuna')
router.register('api/cita',citaMedicaViewSet,'cita')
urlpatterns = router.urls