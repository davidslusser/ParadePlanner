import faker
import random
from model_bakery import baker

from parademgr.models import Award, AwardType, Category, Contact, Division, Address, EmailAddress, Link, Organization, Parade, Participant, PhoneNumber


def create_parades():
    data_list: list = [
        {"title": "Fourth of July Parade", "year": 2022},
        {"title": "Fourth of July Parade", "year": 2023},
        {"title": "Fourth of July Parade", "year": 2024},
        {"title": "Fourth of July Parade", "year": 2025},
    ]
    for data in data_list:
        Parade.objects.get_or_create(**data, defaults=data)


def create_organizations(qty: int = 1) -> None:
    f = faker.Faker()
    for i in range(qty):
        p = f.profile()
        data = {
            "name": p["company"],
            "description": f.paragraph(),
        }
        organization, is_new = Organization.objects.get_or_create(**data, defaults={"name": data["name"]})
        if is_new:
            # create an link address, phone, email, and contact
            phone = PhoneNumber.objects.create(
                number=f.phone_number(), phone_type=random.choices(PhoneNumber.phone_type_choices)
            )
            organization.phone_numbers.add(phone)

            email = EmailAddress.objects.create(
                email=p["mail"], email_address_type=random.choices(EmailAddress.email_address_type_choices)
            )
            organization.emails.add(email)

            address = Address.objects.create(
                street_address=f.street_address(),
                address_extra=f.secondary_address(),
                city=f.city(),
                state=f.state(),
                postal_code=f.postalcode(),
                address_type=random.choices(Address.address_type_choices),
            )
            organization.addresses.add(address)

            contact = Contact.objects.create(
                first_name=f.first_name(), 
                last_name=f.last_name(),
            )
            contact.phone_numbers.add(phone)
            contact.addresses.add(address)
            contact.emails.add(email)
            organization.contacts.add(contact)


def create_parade_participants(qty: int = 1) -> None:
    f = faker.Faker()
    parade = Parade.objects.last()
    for i in range(qty):
        organization = Organization.objects.get_random_row()
        division = Division.objects.get_random_row()
        data = {"parade": parade, 
                "organization": organization, 
                "division": division,
                "entry": random.randint(1,12),
                "march_order": random.randint(1,12),
                "street": f.street_name(),
                }
        Participant.objects.get_or_create(parade=parade, 
                                          organization=organization, 
                                          division=division,
                                          defaults=data)


def create_categories() -> None:
    """ """
    data_list: list = [
        {"name": "Floats", "label": 1, "description": ""},
        {"name": "Bands", "label": 2, "description": ""},
        {"name": "Drum Corps", "label": 3, "description": ""},
        {"name": "Military", "label": 4, "description": ""},
        {"name": "Drill Teams", "label": 5, "description": ""},
        {"name": "Baton Corps", "label": 6, "description": ""},
        {"name": "Vehicles", "label": 7, "description": ""},
        {"name": "Equestrian", "label": 8, "description": ""},
        {"name": "Miscellaneous", "label": 9, "description": ""},
    ]
    for data in data_list:
        Category.objects.get_or_create(name=data["name"], defaults=data)


def create_divisions() -> None:
    """ """
    data_list: list = [
        {
            "category": "Floats", 
            "data": [
                {"name": "Amateur, San Mateo County", "label": "A", "description": ""},
                {"name": "Amateur, Other Communities", "label": "B", "description": ""},
                {"name": "Comm / Municipal, Amateur Built", "label": "C", "description": ""},
                {"name": "Professionally Built", "label": "D", "description": ""},
            ]
        },
        {
            "category": "Bands", 
            "data": [
                {"name": "Youth Marching Band", "label": "A", "description": ""},
                {"name": "Pipe or Fipe Band", "label": "B", "description": ""},
                {"name": "community Band", "label": "C", "description": ""},
            ]
        },
        {
            "category": "Drum Corps", 
            "data": [
                {"name": "Drum and Bugle Corps", "label": "A", "description": ""},
                {"name": "Drum or Drumand Bell Corps", "label": "B", "description": ""},
            ]
        },
        {
            "category": "Military", 
            "data": [
                {"name": "Active", "label": "A", "description": ""},
                {"name": "Reserve", "label": "B", "description": ""},
                {"name": "Guard", "label": "C", "description": ""},
                {"name": "Veterens Group", "label": "D", "description": ""},
            ]
        },
        {
            "category": "Drill Teams", 
            "data": [
                {"name": "Senior Drill or Tall Flags", "label": "A", "description": ""},
                {"name": "Junior Drill or Tall Flags", "label": "B", "description": ""},
                {"name": "Novelty Drill", "label": "C", "description": ""},
                {"name": "Senior Color Guard", "label": "D", "description": ""},
                {"name": "Junior Color Guard", "label": "E", "description": ""},
                {"name": "Senior Drill Captain", "label": "F", "description": ""},
                {"name": "Junior Drill Captain", "label": "G", "description": ""},
            ]
        },
        {
            "category": "Baton Corps", 
            "data": [
                {"name": "Senior Solo", "label": "A", "description": ""},
                {"name": "Junior Solo", "label": "B", "description": ""},
                {"name": "Drum Major", "label": "C", "description": ""},
                {"name": "Senior Corps", "label": "D", "description": ""},
                {"name": "Junior Corps", "label": "E", "description": ""},
            ]
        },
        {
            "category": "Vehicles", 
            "data": [
                {"name": "Vintage Carriage (Pre 1949)", "label": "A", "description": ""},
                {"name": "Vintage Municipal (Pre 1949)", "label": "B", "description": ""},
                {"name": "Vintage Commercial (Pre 1949)", "label": "C", "description": ""},
                {"name": "Classic Vehicle (1950 - 1969)", "label": "D", "description": ""},
                {"name": "Classic Commercial (1950 - 1969)", "label": "E", "description": ""},
            ]
        },
        {
            "category": "Equestrian", 
            "data": [
                {"name": "Mounted Group, w/Color Guard", "label": "A", "description": ""},
                {"name": "Mounted Group, Sheriff's Posse w/ Color Guard", "label": "B", "description": ""},
                {"name": "Open", "label": "C", "description": ""},
            ]
        },
        {
            "category": "Miscellaneous", 
            "data": [
                {"name": "Novelty Individual", "label": "A", "description": ""},
                {"name": "Novelty Group", "label": "B", "description": ""},
                {"name": "Novelty Youth Group", "label": "C", "description": ""},
                {"name": "Community Performance Group", "label": "D", "description": ""},
                {"name": "Commercial Open", "label": "E", "description": ""},
                {"name": "Reenactors", "label": "F", "description": ""},
                {"name": "Fraternal Organizations", "label": "G", "description": ""},
            ]
        },
    ]
    for item in data_list:
        category = Category.objects.get_object_or_none(name=item["category"])
        for data in item["data"]:
            data["category"] = category
            Division.objects.get_or_create(category=category, name=data["name"], defaults=data)


def create_award_types() -> None:
    """ """
    data_list: list = [
        {"name": "cash",  "description": ""},
        {"name": "certificate",  "description": ""},
        {"name": "medal",  "description": ""},
        {"name": "other",  "description": ""},
        {"name": "plaque",  "description": ""},
        {"name": "trophy",  "description": ""},
    ]
    for data in data_list:
        AwardType.objects.get_or_create(name=data["name"], defaults=data)


def create_awards(qty: int = 1) -> None:
    data_list: list = [
        {
            "division": "Amateur, San Mateo County", 
            "data": [
                {"name": "1st Place", "description": "", "award_type": "cash", "amount": 700.00},
                {"name": "2nd Place", "description": "", "award_type": "cash", "amount": 550.00},
                {"name": "3rd Place", "description": "", "award_type": "cash", "amount": 450.00},
                {"name": "4th Place", "description": "", "award_type": "cash", "amount": 300.00},
            ]
        },
        {
            "division": "Amateur, Other Communities", 
            "data": [
                {"name": "1st Place", "description": "", "award_type": "cash", "amount": 350.00},
                {"name": "2nd Place", "description": "", "award_type": "cash", "amount": 250.00},
            ]
        },
        {
            "division": "Comm / Municipal, Amateur Built", 
            "data": [
                {"name": "1st Place", "description": "", "award_type": "cash", "amount": 250.00},
                {"name": "2nd Place", "description": "", "award_type": "cash", "amount": 200.00},
            ]
        },
        {
            "division": "Professionally Built", 
            "data": [
                {"name": "1st Place", "description": "", "award_type": "plaque", "amount": None},
                {"name": "2nd Place", "description": "", "award_type": "plaque", "amount": None},
            ]
        },
    ]
    parade = Parade.objects.last()
    for item in data_list:
        division = Division.objects.get_object_or_none(name=item["division"])
        for data in item["data"]:
            data["division"] = division
            data["award_type"] = AwardType.objects.get_object_or_none(name=data["award_type"])
            Award.objects.get_or_create(division=division, name=data["name"], defaults=data)



def run():
    print("INFO: creating data...")
    create_parades()
    create_organizations(qty=20)
    create_categories()
    create_divisions()
    create_parade_participants(qty=30)
    create_award_types()
    create_awards()
