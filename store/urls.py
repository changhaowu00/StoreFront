from xml.etree.ElementInclude import include
from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter
from pprint import pprint

router = SimpleRouter()
router.register('products',views.ProductViewSet)
router.register('collection',views.CollectionViewSet)
pprint(router.urls)

# URLConf
urlpatterns = router.urls
