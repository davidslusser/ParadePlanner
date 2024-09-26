""" filtersets for applicable app models """

from rest_framework_filters.filters import RelatedFilter, BooleanFilter
from rest_framework_filters.filterset import FilterSet

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


class AddressFilterSet(FilterSet):
    """filterset class for Address"""
    contact = RelatedFilter('ContactFilterSet', field_name='contact', queryset=Contact.objects.all())
    has_contact = BooleanFilter(field_name='contact', lookup_expr='isnull', exclude=True)
    organization = RelatedFilter('OrganizationFilterSet', field_name='organization', queryset=Organization.objects.all())
    has_organization = BooleanFilter(field_name='organization', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Address
        fields = {
            'address_extra': '__all__',        
            'address_type': '__all__',        
            'city': '__all__',        
            'created_at': '__all__',        
            'id': '__all__',        
            'postal_code': '__all__',        
            'state': '__all__',        
            'street_address': '__all__',        
            'updated_at': '__all__',        
        }
        

class AwardFilterSet(FilterSet):
    """filterset class for Award"""
    award_type = RelatedFilter('AwardTypeFilterSet', field_name='award_type', queryset=AwardType.objects.all())
    division = RelatedFilter('DivisionFilterSet', field_name='division', queryset=Division.objects.all())
    participantaward = RelatedFilter('ParticipantAwardFilterSet', field_name='participantaward', queryset=ParticipantAward.objects.all())
    has_participantaward = BooleanFilter(field_name='participantaward', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Award
        fields = {
            'amount': '__all__',        
            'award_type': '__all__',        
            'created_at': '__all__',        
            'description': '__all__',        
            'division': '__all__',        
            'id': '__all__',        
            'name': '__all__',        
            'updated_at': '__all__',        
        }
        

class AwardTypeFilterSet(FilterSet):
    """filterset class for AwardType"""
    award = RelatedFilter('AwardFilterSet', field_name='award', queryset=Award.objects.all())
    has_award = BooleanFilter(field_name='award', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = AwardType
        fields = {
            'created_at': '__all__',        
            'description': '__all__',        
            'enabled': '__all__',        
            'id': '__all__',        
            'name': '__all__',        
            'updated_at': '__all__',        
        }
        

class CategoryFilterSet(FilterSet):
    """filterset class for Category"""
    division = RelatedFilter('DivisionFilterSet', field_name='division', queryset=Division.objects.all())
    has_division = BooleanFilter(field_name='division', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Category
        fields = {
            'created_at': '__all__',        
            'description': '__all__',        
            'enabled': '__all__',        
            'id': '__all__',        
            'label': '__all__',        
            'name': '__all__',        
            'updated_at': '__all__',        
        }
        

class ContactFilterSet(FilterSet):
    """filterset class for Contact"""
    organization = RelatedFilter('OrganizationFilterSet', field_name='organization', queryset=Organization.objects.all())
    has_organization = BooleanFilter(field_name='organization', lookup_expr='isnull', exclude=True)
    addresses = RelatedFilter('AddressFilterSet', field_name='addresses', queryset=Address.objects.all())
    has_addresses = BooleanFilter(field_name='addresses', lookup_expr='isnull', exclude=True)
    emails = RelatedFilter('EmailAddressFilterSet', field_name='emails', queryset=EmailAddress.objects.all())
    has_emails = BooleanFilter(field_name='emails', lookup_expr='isnull', exclude=True)
    links = RelatedFilter('LinkFilterSet', field_name='links', queryset=Link.objects.all())
    has_links = BooleanFilter(field_name='links', lookup_expr='isnull', exclude=True)
    phone_numbers = RelatedFilter('PhoneNumberFilterSet', field_name='phone_numbers', queryset=PhoneNumber.objects.all())
    has_phone_numbers = BooleanFilter(field_name='phone_numbers', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Contact
        fields = {
            'created_at': '__all__',        
            'first_name': '__all__',        
            'id': '__all__',        
            'last_name': '__all__',        
            'updated_at': '__all__',        
        }
        

class DivisionFilterSet(FilterSet):
    """filterset class for Division"""
    category = RelatedFilter('CategoryFilterSet', field_name='category', queryset=Category.objects.all())
    award = RelatedFilter('AwardFilterSet', field_name='award', queryset=Award.objects.all())
    has_award = BooleanFilter(field_name='award', lookup_expr='isnull', exclude=True)
    participant = RelatedFilter('ParticipantFilterSet', field_name='participant', queryset=Participant.objects.all())
    has_participant = BooleanFilter(field_name='participant', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Division
        fields = {
            'category': '__all__',        
            'created_at': '__all__',        
            'description': '__all__',        
            'enabled': '__all__',        
            'id': '__all__',        
            'label': '__all__',        
            'name': '__all__',        
            'updated_at': '__all__',        
        }
        

class EmailAddressFilterSet(FilterSet):
    """filterset class for EmailAddress"""
    contact = RelatedFilter('ContactFilterSet', field_name='contact', queryset=Contact.objects.all())
    has_contact = BooleanFilter(field_name='contact', lookup_expr='isnull', exclude=True)
    organization = RelatedFilter('OrganizationFilterSet', field_name='organization', queryset=Organization.objects.all())
    has_organization = BooleanFilter(field_name='organization', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = EmailAddress
        fields = {
            'created_at': '__all__',        
            'email': '__all__',        
            'email_address_type': '__all__',        
            'id': '__all__',        
            'updated_at': '__all__',        
        }
        

class LinkFilterSet(FilterSet):
    """filterset class for Link"""
    contact = RelatedFilter('ContactFilterSet', field_name='contact', queryset=Contact.objects.all())
    has_contact = BooleanFilter(field_name='contact', lookup_expr='isnull', exclude=True)
    organization = RelatedFilter('OrganizationFilterSet', field_name='organization', queryset=Organization.objects.all())
    has_organization = BooleanFilter(field_name='organization', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Link
        fields = {
            'created_at': '__all__',        
            'description': '__all__',        
            'id': '__all__',        
            'name': '__all__',        
            'updated_at': '__all__',        
            'url': '__all__',        
        }
        

class OrganizationFilterSet(FilterSet):
    """filterset class for Organization"""
    participant = RelatedFilter('ParticipantFilterSet', field_name='participant', queryset=Participant.objects.all())
    has_participant = BooleanFilter(field_name='participant', lookup_expr='isnull', exclude=True)
    addresses = RelatedFilter('AddressFilterSet', field_name='addresses', queryset=Address.objects.all())
    has_addresses = BooleanFilter(field_name='addresses', lookup_expr='isnull', exclude=True)
    contacts = RelatedFilter('ContactFilterSet', field_name='contacts', queryset=Contact.objects.all())
    has_contacts = BooleanFilter(field_name='contacts', lookup_expr='isnull', exclude=True)
    emails = RelatedFilter('EmailAddressFilterSet', field_name='emails', queryset=EmailAddress.objects.all())
    has_emails = BooleanFilter(field_name='emails', lookup_expr='isnull', exclude=True)
    links = RelatedFilter('LinkFilterSet', field_name='links', queryset=Link.objects.all())
    has_links = BooleanFilter(field_name='links', lookup_expr='isnull', exclude=True)
    phone_numbers = RelatedFilter('PhoneNumberFilterSet', field_name='phone_numbers', queryset=PhoneNumber.objects.all())
    has_phone_numbers = BooleanFilter(field_name='phone_numbers', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Organization
        fields = {
            'created_at': '__all__',        
            'description': '__all__',        
            'id': '__all__',        
            'name': '__all__',        
            'updated_at': '__all__',        
        }
        

class ParadeFilterSet(FilterSet):
    """filterset class for Parade"""
    participant = RelatedFilter('ParticipantFilterSet', field_name='participant', queryset=Participant.objects.all())
    has_participant = BooleanFilter(field_name='participant', lookup_expr='isnull', exclude=True)
    participantaward = RelatedFilter('ParticipantAwardFilterSet', field_name='participantaward', queryset=ParticipantAward.objects.all())
    has_participantaward = BooleanFilter(field_name='participantaward', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Parade
        fields = {
            'created_at': '__all__',        
            'id': '__all__',        
            'title': '__all__',        
            'updated_at': '__all__',        
            'year': '__all__',        
        }
        

class ParticipantFilterSet(FilterSet):
    """filterset class for Participant"""
    division = RelatedFilter('DivisionFilterSet', field_name='division', queryset=Division.objects.all())
    organization = RelatedFilter('OrganizationFilterSet', field_name='organization', queryset=Organization.objects.all())
    parade = RelatedFilter('ParadeFilterSet', field_name='parade', queryset=Parade.objects.all())
    participantaward = RelatedFilter('ParticipantAwardFilterSet', field_name='participantaward', queryset=ParticipantAward.objects.all())
    has_participantaward = BooleanFilter(field_name='participantaward', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Participant
        fields = {
            'created_at': '__all__',        
            'division': '__all__',        
            'entry': '__all__',        
            'id': '__all__',        
            'march_order': '__all__',        
            'organization': '__all__',        
            'parade': '__all__',        
            'street': '__all__',        
            'updated_at': '__all__',        
        }
        

class ParticipantAwardFilterSet(FilterSet):
    """filterset class for ParticipantAward"""
    award = RelatedFilter('AwardFilterSet', field_name='award', queryset=Award.objects.all())
    parade = RelatedFilter('ParadeFilterSet', field_name='parade', queryset=Parade.objects.all())
    winner = RelatedFilter('ParticipantFilterSet', field_name='winner', queryset=Participant.objects.all())

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = ParticipantAward
        fields = {
            'award': '__all__',        
            'created_at': '__all__',        
            'id': '__all__',        
            'parade': '__all__',        
            'updated_at': '__all__',        
            'winner': '__all__',        
        }
        

class PhoneNumberFilterSet(FilterSet):
    """filterset class for PhoneNumber"""
    contact = RelatedFilter('ContactFilterSet', field_name='contact', queryset=Contact.objects.all())
    has_contact = BooleanFilter(field_name='contact', lookup_expr='isnull', exclude=True)
    organization = RelatedFilter('OrganizationFilterSet', field_name='organization', queryset=Organization.objects.all())
    has_organization = BooleanFilter(field_name='organization', lookup_expr='isnull', exclude=True)

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = PhoneNumber
        fields = {
            'created_at': '__all__',        
            'id': '__all__',        
            'number': '__all__',        
            'phone_type': '__all__',        
            'updated_at': '__all__',        
        }
        