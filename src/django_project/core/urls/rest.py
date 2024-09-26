from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from parademgr.views import rest

app_name = "rest"

router = routers.DefaultRouter()


router.register(r'address', rest.AddressViewSet, 'address')
router.register(r'award', rest.AwardViewSet, 'award')
router.register(r'awardtype', rest.AwardTypeViewSet, 'awardtype')
router.register(r'category', rest.CategoryViewSet, 'category')
router.register(r'contact', rest.ContactViewSet, 'contact')
router.register(r'division', rest.DivisionViewSet, 'division')
router.register(r'emailaddress', rest.EmailAddressViewSet, 'emailaddress')
router.register(r'link', rest.LinkViewSet, 'link')
router.register(r'organization', rest.OrganizationViewSet, 'organization')
router.register(r'parade', rest.ParadeViewSet, 'parade')
router.register(r'participant', rest.ParticipantViewSet, 'participant')
router.register(r'participantaward', rest.ParticipantAwardViewSet, 'participantaward')
router.register(r'phonenumber', rest.PhoneNumberViewSet, 'phonenumber')


urlpatterns = [
    # API views
    path("", include(router.urls)),
    path("v1/", include(router.urls)),
]
