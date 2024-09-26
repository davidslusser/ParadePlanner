""" DRF viewsets for applicable app models """

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_flex_fields import is_expanded

# import models
from parademgr.models import (Address,
                              Award,
                              AwardType,
                              Category,
                              Contact,
                              Division,
                              EmailAddress,
                              Link,
                              Organization,
                              Parade,
                              Participant,
                              ParticipantAward,
                              PhoneNumber
                              )

# import serializers
from parademgr.serializers import (AddressSerializer,
                                   AwardSerializer,
                                   AwardTypeSerializer,
                                   CategorySerializer,
                                   ContactSerializer,
                                   DivisionSerializer,
                                   EmailAddressSerializer,
                                   LinkSerializer,
                                   OrganizationSerializer,
                                   ParadeSerializer,
                                   ParticipantSerializer,
                                   ParticipantAwardSerializer,
                                   PhoneNumberSerializer
                                   )

# import filtersets
from parademgr.filtersets import (AddressFilterSet,
                                  AwardFilterSet,
                                  AwardTypeFilterSet,
                                  CategoryFilterSet,
                                  ContactFilterSet,
                                  DivisionFilterSet,
                                  EmailAddressFilterSet,
                                  LinkFilterSet,
                                  OrganizationFilterSet,
                                  ParadeFilterSet,
                                  ParticipantFilterSet,
                                  ParticipantAwardFilterSet,
                                  PhoneNumberFilterSet
                                  )


class AddressViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows Addresss to be viewed """
    model = Address
    queryset = model.objects.all()
    serializer_class = AddressSerializer
    filterset_class = AddressFilterSet
    
    @action(detail=True, methods=['get'])
    def contact_set(self, request, *args, **kwargs):
        """ get the contacts associated with this Address instance if available """
        instance = self.get_object()
        data = instance.contact_set.all()
        if data:
            try:
                serializer = ContactSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No contacts available for this address ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def organization_set(self, request, *args, **kwargs):
        """ get the organizations associated with this Address instance if available """
        instance = self.get_object()
        data = instance.organization_set.all()
        if data:
            try:
                serializer = OrganizationSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No organizations available for this address ', status.HTTP_404_NOT_FOUND)
    

class AwardViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows Awards to be viewed """
    model = Award
    serializer_class = AwardSerializer
    filterset_class = AwardFilterSet
    
    @action(detail=True, methods=['get'])
    def participantaward_set(self, request, *args, **kwargs):
        """ get the participantawards associated with this Award instance if available """
        instance = self.get_object()
        data = instance.participantaward_set.all()
        if data:
            try:
                serializer = ParticipantAwardSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No participantawards available for this award ', status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self):
        queryset = self.model.objects.all().select_related('award_type', 'division', )
        
        if is_expanded(self.request, 'award_type'):
            queryset = queryset.select_related('award_type')
            
        if is_expanded(self.request, 'division'):
            queryset = queryset.select_related('division__category', )
            
        return queryset
    

class AwardTypeViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows AwardTypes to be viewed """
    model = AwardType
    queryset = model.objects.all()
    serializer_class = AwardTypeSerializer
    filterset_class = AwardTypeFilterSet
    
    @action(detail=True, methods=['get'])
    def award_set(self, request, *args, **kwargs):
        """ get the awards associated with this AwardType instance if available """
        instance = self.get_object()
        data = instance.award_set.all()
        if data:
            try:
                serializer = AwardSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No awards available for this awardtype ', status.HTTP_404_NOT_FOUND)
    

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows Categorys to be viewed """
    model = Category
    queryset = model.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilterSet
    
    @action(detail=True, methods=['get'])
    def division_set(self, request, *args, **kwargs):
        """ get the divisions associated with this Category instance if available """
        instance = self.get_object()
        data = instance.division_set.all()
        if data:
            try:
                serializer = DivisionSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No divisions available for this category ', status.HTTP_404_NOT_FOUND)
    

class ContactViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows Contacts to be viewed """
    model = Contact
    queryset = model.objects.all()
    serializer_class = ContactSerializer
    filterset_class = ContactFilterSet
    
    @action(detail=True, methods=['get'])
    def organization_set(self, request, *args, **kwargs):
        """ get the organizations associated with this Contact instance if available """
        instance = self.get_object()
        data = instance.organization_set.all()
        if data:
            try:
                serializer = OrganizationSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No organizations available for this contact ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def addresses(self, request, *args, **kwargs):
        """ get the addressess associated with this Contact instance if available """
        instance = self.get_object()
        data = instance.addresses.all()
        if data:
            try:
                serializer = AddressSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No addressess available for this contact ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def emails(self, request, *args, **kwargs):
        """ get the emailss associated with this Contact instance if available """
        instance = self.get_object()
        data = instance.emails.all()
        if data:
            try:
                serializer = EmailAddressSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No emailss available for this contact ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def links(self, request, *args, **kwargs):
        """ get the linkss associated with this Contact instance if available """
        instance = self.get_object()
        data = instance.links.all()
        if data:
            try:
                serializer = LinkSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No linkss available for this contact ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def phone_numbers(self, request, *args, **kwargs):
        """ get the phone_numberss associated with this Contact instance if available """
        instance = self.get_object()
        data = instance.phone_numbers.all()
        if data:
            try:
                serializer = PhoneNumberSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No phone_numberss available for this contact ', status.HTTP_404_NOT_FOUND)
    

class DivisionViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows Divisions to be viewed """
    model = Division
    serializer_class = DivisionSerializer
    filterset_class = DivisionFilterSet
    
    @action(detail=True, methods=['get'])
    def award_set(self, request, *args, **kwargs):
        """ get the awards associated with this Division instance if available """
        instance = self.get_object()
        data = instance.award_set.all()
        if data:
            try:
                serializer = AwardSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No awards available for this division ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def participant_set(self, request, *args, **kwargs):
        """ get the participants associated with this Division instance if available """
        instance = self.get_object()
        data = instance.participant_set.all()
        if data:
            try:
                serializer = ParticipantSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No participants available for this division ', status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self):
        queryset = self.model.objects.all().select_related('category', )
        
        if is_expanded(self.request, 'category'):
            queryset = queryset.select_related('category')
            
        return queryset
    

class EmailAddressViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows EmailAddresss to be viewed """
    model = EmailAddress
    queryset = model.objects.all()
    serializer_class = EmailAddressSerializer
    filterset_class = EmailAddressFilterSet
    
    @action(detail=True, methods=['get'])
    def contact_set(self, request, *args, **kwargs):
        """ get the contacts associated with this EmailAddress instance if available """
        instance = self.get_object()
        data = instance.contact_set.all()
        if data:
            try:
                serializer = ContactSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No contacts available for this emailaddress ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def organization_set(self, request, *args, **kwargs):
        """ get the organizations associated with this EmailAddress instance if available """
        instance = self.get_object()
        data = instance.organization_set.all()
        if data:
            try:
                serializer = OrganizationSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No organizations available for this emailaddress ', status.HTTP_404_NOT_FOUND)
    

class LinkViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows Links to be viewed """
    model = Link
    queryset = model.objects.all()
    serializer_class = LinkSerializer
    filterset_class = LinkFilterSet
    
    @action(detail=True, methods=['get'])
    def contact_set(self, request, *args, **kwargs):
        """ get the contacts associated with this Link instance if available """
        instance = self.get_object()
        data = instance.contact_set.all()
        if data:
            try:
                serializer = ContactSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No contacts available for this link ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def organization_set(self, request, *args, **kwargs):
        """ get the organizations associated with this Link instance if available """
        instance = self.get_object()
        data = instance.organization_set.all()
        if data:
            try:
                serializer = OrganizationSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No organizations available for this link ', status.HTTP_404_NOT_FOUND)
    

class OrganizationViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows Organizations to be viewed """
    model = Organization
    queryset = model.objects.all()
    serializer_class = OrganizationSerializer
    filterset_class = OrganizationFilterSet
    
    @action(detail=True, methods=['get'])
    def participant_set(self, request, *args, **kwargs):
        """ get the participants associated with this Organization instance if available """
        instance = self.get_object()
        data = instance.participant_set.all()
        if data:
            try:
                serializer = ParticipantSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No participants available for this organization ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def addresses(self, request, *args, **kwargs):
        """ get the addressess associated with this Organization instance if available """
        instance = self.get_object()
        data = instance.addresses.all()
        if data:
            try:
                serializer = AddressSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No addressess available for this organization ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def contacts(self, request, *args, **kwargs):
        """ get the contactss associated with this Organization instance if available """
        instance = self.get_object()
        data = instance.contacts.all()
        if data:
            try:
                serializer = ContactSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No contactss available for this organization ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def emails(self, request, *args, **kwargs):
        """ get the emailss associated with this Organization instance if available """
        instance = self.get_object()
        data = instance.emails.all()
        if data:
            try:
                serializer = EmailAddressSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No emailss available for this organization ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def links(self, request, *args, **kwargs):
        """ get the linkss associated with this Organization instance if available """
        instance = self.get_object()
        data = instance.links.all()
        if data:
            try:
                serializer = LinkSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No linkss available for this organization ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def phone_numbers(self, request, *args, **kwargs):
        """ get the phone_numberss associated with this Organization instance if available """
        instance = self.get_object()
        data = instance.phone_numbers.all()
        if data:
            try:
                serializer = PhoneNumberSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No phone_numberss available for this organization ', status.HTTP_404_NOT_FOUND)
    

class ParadeViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows Parades to be viewed """
    model = Parade
    queryset = model.objects.all()
    serializer_class = ParadeSerializer
    filterset_class = ParadeFilterSet
    
    @action(detail=True, methods=['get'])
    def participant_set(self, request, *args, **kwargs):
        """ get the participants associated with this Parade instance if available """
        instance = self.get_object()
        data = instance.participant_set.all()
        if data:
            try:
                serializer = ParticipantSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No participants available for this parade ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def participantaward_set(self, request, *args, **kwargs):
        """ get the participantawards associated with this Parade instance if available """
        instance = self.get_object()
        data = instance.participantaward_set.all()
        if data:
            try:
                serializer = ParticipantAwardSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No participantawards available for this parade ', status.HTTP_404_NOT_FOUND)
    

class ParticipantViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows Participants to be viewed """
    model = Participant
    serializer_class = ParticipantSerializer
    filterset_class = ParticipantFilterSet
    
    @action(detail=True, methods=['get'])
    def participantaward_set(self, request, *args, **kwargs):
        """ get the participantawards associated with this Participant instance if available """
        instance = self.get_object()
        data = instance.participantaward_set.all()
        if data:
            try:
                serializer = ParticipantAwardSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No participantawards available for this participant ', status.HTTP_404_NOT_FOUND)
    
    def get_queryset(self):
        queryset = self.model.objects.all().select_related('division', 'organization', 'parade', )
        
        if is_expanded(self.request, 'division'):
            queryset = queryset.select_related('division__category', )
            
        if is_expanded(self.request, 'organization'):
            queryset = queryset.select_related('organization')
            
        if is_expanded(self.request, 'parade'):
            queryset = queryset.select_related('parade')
            
        return queryset
    

class ParticipantAwardViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows ParticipantAwards to be viewed """
    model = ParticipantAward
    serializer_class = ParticipantAwardSerializer
    filterset_class = ParticipantAwardFilterSet
    
    def get_queryset(self):
        queryset = self.model.objects.all().select_related('award', 'parade', 'winner', )
        
        if is_expanded(self.request, 'award'):
            queryset = queryset.select_related('award__award_type', 'award__division', )
            
        if is_expanded(self.request, 'parade'):
            queryset = queryset.select_related('parade')
            
        if is_expanded(self.request, 'winner'):
            queryset = queryset.select_related('winner__parade', 'winner__organization', 'winner__division', )
            
        return queryset
    

class PhoneNumberViewSet(viewsets.ReadOnlyModelViewSet):
    """ API endpoint that allows PhoneNumbers to be viewed """
    model = PhoneNumber
    queryset = model.objects.all()
    serializer_class = PhoneNumberSerializer
    filterset_class = PhoneNumberFilterSet
    
    @action(detail=True, methods=['get'])
    def contact_set(self, request, *args, **kwargs):
        """ get the contacts associated with this PhoneNumber instance if available """
        instance = self.get_object()
        data = instance.contact_set.all()
        if data:
            try:
                serializer = ContactSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No contacts available for this phonenumber ', status.HTTP_404_NOT_FOUND)
    
    @action(detail=True, methods=['get'])
    def organization_set(self, request, *args, **kwargs):
        """ get the organizations associated with this PhoneNumber instance if available """
        instance = self.get_object()
        data = instance.organization_set.all()
        if data:
            try:
                serializer = OrganizationSerializer(data, many=True)
                return Response(serializer.data, status.HTTP_200_OK)
            except Exception as err:
                return Response(str(err), status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response('No organizations available for this phonenumber ', status.HTTP_404_NOT_FOUND)
    