from django.urls import include, path
from rest_framework import routers
from rest import views

router = routers.DefaultRouter()
router.register(r'manufacturers', views.ManufacturerViewSet)
router.register(r'shoetypes', views.ShoeTypeViewSet)
router.register(r'shoecolors', views.ShoeColorViewSet)
router.register(r'shoes', views.ShoeViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]