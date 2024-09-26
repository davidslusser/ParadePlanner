from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from parademgr.views import rest

router = routers.DefaultRouter()


# parademgr API Endpoints
# router.register(r"model_name", rest.ModelViewSet, "model_name")
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
    path("rest/", include(router.urls)),
]
