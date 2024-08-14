from django.db import models
from django.urls import reverse
from auditlog.registry import auditlog
from handyhelpers.models import HandyHelperBaseModel
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Organization(HandyHelperBaseModel):
    """ """
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=255, blank=True)
    phone_numbers = models.ManyToManyField("PhoneNumber", blank=True)
    addresses = models.ManyToManyField("Address", blank=True)
    links = models.ManyToManyField("Link", blank=True)
    emails = models.ManyToManyField("EmailAddress", blank=True)
    contacts = models.ManyToManyField("Contact", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Organizations"


class Contact(HandyHelperBaseModel):
    """ """
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_numbers = models.ManyToManyField("PhoneNumber", blank=True)
    addresses = models.ManyToManyField("Address", blank=True)
    links = models.ManyToManyField("Link", blank=True)
    emails = models.ManyToManyField("EmailAddress", blank=True)


class Address(HandyHelperBaseModel):
    address_type_choices = [
        ("Corporate", "Corporate"),
        ("Branch", "Branch"),
        ("Home", "Home"),
        ("Other", "Other"),
    ]

    street_address = models.CharField(max_length=255)
    address_extra = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    address_type = models.CharField(max_length=16, blank=True, choices=address_type_choices)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state} {self.postal_code}"


class PhoneNumber(HandyHelperBaseModel):

    phone_type_choices = [
        ("Direct", "Direct"),
        ("Fax", "Fax"),
        ("Home", "Home"),
        ("Mobile", "Mobile"),
        ("Office", "Office"),
        ("Other", "Other"),
    ]

    number = PhoneNumberField(null=False, blank=False, unique=True)
    phone_type = models.CharField(max_length=16, blank=True, choices=phone_type_choices)

    def __str__(self):
        return str(self.number)


class EmailAddress(HandyHelperBaseModel):
    email_address_type_choices = [
        ("Direct", "Direct"),
        ("Work", "Work"),
        ("Personal", "Personal"),
        ("Other", "Other"),
    ]
    email = models.EmailField(unique=True)
    email_address_type = models.CharField(max_length=16, blank=True, choices=email_address_type_choices)

    def __str__(self):
        return str(self.email)


class Link(HandyHelperBaseModel):
    name = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=255, blank=True)
    url = models.URLField()

    def __str__(self):
        return self.url


class Parade(HandyHelperBaseModel):
    """ """
    current_year = timezone.datetime.now().year
    title = models.CharField(max_length=64, blank=True)
    year = models.IntegerField(
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(current_year + 5)
        ],
        help_text="Enter a valid year"
    )

    def __str__(self):
        return f"{self.year} {self.title}"

    # class Meta:
    #     verbose_name_plural = "Parades"

    def get_awards(self):
        """ """
        return ParticipantAward.objects.filter(parade=self).select_related("award", "award__division", "award__division__category", "award__award_type", "parade", "winner")


    def get_participants(self):
        """ """
        return Participant.objects.filter(parade=self).select_related("division", "division__category", "organization", "parade")


class Category(HandyHelperBaseModel):
    """ """
    name = models.CharField(max_length=32, unique=True)
    label = models.CharField(max_length=2, unique=True)
    description = models.CharField(max_length=255, blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', 'label']
        verbose_name_plural = "Categories"


class Division(HandyHelperBaseModel):
    """ """
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    label = models.CharField(max_length=2)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (("category", "name"), )
        ordering = ['category', 'label']


class Participant(HandyHelperBaseModel):
    """ """
    parade = models.ForeignKey("Parade", on_delete=models.CASCADE)
    organization = models.ForeignKey("Organization", on_delete=models.CASCADE)
    division = models.ForeignKey("Division", on_delete=models.CASCADE)
    entry = models.IntegerField(blank=True, null=True)
    street = models.CharField(max_length=32, null=True)
    march_order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.organization.name


class AwardType(HandyHelperBaseModel):
    """ """
    name = models.CharField(max_length=32, unique=True)
    description = models.CharField(max_length=255, blank=True)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Award(HandyHelperBaseModel):
    """ """ 
    award_type = models.ForeignKey("AwardType", on_delete=models.CASCADE)
    division = models.ForeignKey("Division", blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=255, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.division} - {self.name}" if self.division else self.name

    class Meta:
        unique_together = (("division", "name"), )


class ParticipantAward(HandyHelperBaseModel):
    award = models.ForeignKey("Award", on_delete=models.CASCADE)
    parade = models.ForeignKey("Parade", on_delete=models.CASCADE)
    winner = models.ForeignKey("Participant", blank=True, null=True, on_delete=models.CASCADE)


# register models with auditlog
# auditlog.register(MyModel)
