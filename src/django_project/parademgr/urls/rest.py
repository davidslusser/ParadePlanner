from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from parademgr.views import rest

router = routers.DefaultRouter()


# parademgr API Endpoints
# router.register(r"model_name", rest.ModelViewSet, "model_name")


urlpatterns = [
    # API views
    path("rest/", include(router.urls)),
]
