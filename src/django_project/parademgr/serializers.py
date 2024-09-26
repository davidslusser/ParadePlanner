""" DRF serailizers for applicable app models """

from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer


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


class AddressSerializer(FlexFieldsModelSerializer):
    """serializer class for Address"""

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Address
        fields = [
            'address_extra',
            'address_type',
            'city',
            'created_at',
            'id',
            'postal_code',
            'state',
            'street_address',
            'updated_at',
        ]
        

class AwardSerializer(FlexFieldsModelSerializer):
    """serializer class for Award"""
    award_type = serializers.StringRelatedField()
    division = serializers.StringRelatedField()

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Award
        fields = [
            'amount',
            'award_type',
            'created_at',
            'description',
            'division',
            'id',
            'name',
            'updated_at',
        ]
        
        expandable_fields = {
            'award_type': 'parademgr../serializers.AwardTypeSerializer',
            'division': 'parademgr../serializers.DivisionSerializer',
        }
        

class AwardTypeSerializer(FlexFieldsModelSerializer):
    """serializer class for AwardType"""

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = AwardType
        fields = [
            'created_at',
            'description',
            'enabled',
            'id',
            'name',
            'updated_at',
        ]
        

class CategorySerializer(FlexFieldsModelSerializer):
    """serializer class for Category"""

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Category
        fields = [
            'created_at',
            'description',
            'enabled',
            'id',
            'label',
            'name',
            'updated_at',
        ]
        

class ContactSerializer(FlexFieldsModelSerializer):
    """serializer class for Contact"""

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Contact
        fields = [
            'created_at',
            'first_name',
            'id',
            'last_name',
            'updated_at',
        ]
        

class DivisionSerializer(FlexFieldsModelSerializer):
    """serializer class for Division"""
    category = serializers.StringRelatedField()

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Division
        fields = [
            'category',
            'created_at',
            'description',
            'enabled',
            'id',
            'label',
            'name',
            'updated_at',
        ]
        
        expandable_fields = {
            'category': 'parademgr../serializers.CategorySerializer',
        }
        

class EmailAddressSerializer(FlexFieldsModelSerializer):
    """serializer class for EmailAddress"""

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = EmailAddress
        fields = [
            'created_at',
            'email',
            'email_address_type',
            'id',
            'updated_at',
        ]
        

class LinkSerializer(FlexFieldsModelSerializer):
    """serializer class for Link"""

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Link
        fields = [
            'created_at',
            'description',
            'id',
            'name',
            'updated_at',
            'url',
        ]
        

class OrganizationSerializer(FlexFieldsModelSerializer):
    """serializer class for Organization"""

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Organization
        fields = [
            'created_at',
            'description',
            'id',
            'name',
            'updated_at',
        ]
        

class ParadeSerializer(FlexFieldsModelSerializer):
    """serializer class for Parade"""

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Parade
        fields = [
            'created_at',
            'id',
            'title',
            'updated_at',
            'year',
        ]
        

class ParticipantSerializer(FlexFieldsModelSerializer):
    """serializer class for Participant"""
    division = serializers.StringRelatedField()
    organization = serializers.StringRelatedField()
    parade = serializers.StringRelatedField()

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = Participant
        fields = [
            'created_at',
            'division',
            'entry',
            'id',
            'march_order',
            'organization',
            'parade',
            'street',
            'updated_at',
        ]
        
        expandable_fields = {
            'division': 'parademgr../serializers.DivisionSerializer',
            'organization': 'parademgr../serializers.OrganizationSerializer',
            'parade': 'parademgr../serializers.ParadeSerializer',
        }
        

class ParticipantAwardSerializer(FlexFieldsModelSerializer):
    """serializer class for ParticipantAward"""
    award = serializers.StringRelatedField()
    parade = serializers.StringRelatedField()
    winner = serializers.StringRelatedField()

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = ParticipantAward
        fields = [
            'award',
            'created_at',
            'id',
            'parade',
            'updated_at',
            'winner',
        ]
        
        expandable_fields = {
            'award': 'parademgr../serializers.AwardSerializer',
            'parade': 'parademgr../serializers.ParadeSerializer',
            'winner': 'parademgr../serializers.ParticipantSerializer',
        }
        

class PhoneNumberSerializer(FlexFieldsModelSerializer):
    """serializer class for PhoneNumber"""

    class Meta:
        """Metaclass to define filterset model and fields"""
        model = PhoneNumber
        fields = [
            'created_at',
            'id',
            'number',
            'phone_type',
            'updated_at',
        ]
        