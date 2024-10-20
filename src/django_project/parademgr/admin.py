from django.contrib import admin

# import models
from parademgr.models import (
    Address,
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
    PhoneNumber,
)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "name", "description"]
    search_fields = ["id", "name", "description"]
    list_filter = []


class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "first_name", "last_name"]
    search_fields = ["id", "first_name", "last_name"]
    list_filter = []


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "created_at",
        "updated_at",
        "street_address",
        "address_extra",
        "city",
        "state",
        "postal_code",
        "address_type",
    ]
    search_fields = ["id", "street_address", "address_extra", "city", "state", "postal_code", "address_type"]
    list_filter = ["address_type"]


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "number", "phone_type"]
    search_fields = ["id", "number", "phone_type"]
    list_filter = ["phone_type"]


class EmailAddressAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "email", "email_address_type"]
    search_fields = ["id", "email", "email_address_type"]
    list_filter = ["email_address_type"]


class LinkAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "name", "description", "url"]
    search_fields = ["id", "name", "description", "url"]
    list_filter = []


class ParadeAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "title", "year"]
    search_fields = ["id", "title", "year"]
    list_filter = []


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "name", "label", "description", "enabled"]
    search_fields = ["id", "name", "label", "description"]
    list_filter = ["enabled"]


class DivisionAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "category", "label", "name", "description", "enabled"]
    search_fields = ["id", "label", "name", "description"]
    list_filter = ["category", "enabled"]


class ParticipantAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "created_at",
        "updated_at",
        "parade",
        "organization",
        "division",
        "entry",
        "street",
        "march_order",
    ]
    search_fields = ["id", "entry", "street", "march_order"]
    list_filter = ["parade", "organization", "division"]


class AwardTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "name", "description", "enabled"]
    search_fields = ["id", "name", "description"]
    list_filter = ["enabled"]


class AwardAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "award_type", "division", "name", "description", "amount"]
    search_fields = ["id", "name", "description", "amount"]
    list_filter = ["award_type", "division"]


class ParticipantAwardAdmin(admin.ModelAdmin):
    list_display = ["id", "created_at", "updated_at", "award", "parade", "winner"]
    search_fields = ["id"]
    list_filter = ["award", "parade", "winner"]


# register models
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
admin.site.register(EmailAddress, EmailAddressAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Parade, ParadeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Division, DivisionAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(AwardType, AwardTypeAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(ParticipantAward, ParticipantAwardAdmin)
