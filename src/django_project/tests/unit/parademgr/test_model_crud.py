import django
import os
import random
from django.apps import apps
from django.test import TestCase
from model_bakery import baker
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()


class AddressTests(TestCase):
    """ test CRUD operations on Address """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'address')
        self.to_bake = 'parademgr.Address'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, _fill_optional=['address_extra', 'address_type'])

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_address_extra(self):
        """ verify address_extra (CharField) can be updated """
        row = self.bake()
        original_value = row.address_extra
        updated_value = baker.prepare(self.to_bake, _fill_optional=['address_extra']).address_extra
        setattr(row, 'address_extra', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'address_extra'), updated_value)
        self.assertNotEqual(getattr(row, 'address_extra'), original_value)
    
    def test_update_address_type(self):
        """ verify address_type (CharField) can be updated """
        row = self.bake()
        original_value = row.address_type
        choices = getattr(self.model.address_type.field, 'choices', None)
        updated_value = random.choice([i[0] for i in choices if original_value not in i])
        setattr(row, 'address_type', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'address_type'), updated_value)
        self.assertNotEqual(getattr(row, 'address_type'), original_value)
    
    def test_update_city(self):
        """ verify city (CharField) can be updated """
        row = self.bake()
        original_value = row.city
        updated_value = baker.prepare(self.to_bake, _fill_optional=['city']).city
        setattr(row, 'city', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'city'), updated_value)
        self.assertNotEqual(getattr(row, 'city'), original_value)
    
    def test_update_postal_code(self):
        """ verify postal_code (CharField) can be updated """
        row = self.bake()
        original_value = row.postal_code
        updated_value = baker.prepare(self.to_bake, _fill_optional=['postal_code']).postal_code
        setattr(row, 'postal_code', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'postal_code'), updated_value)
        self.assertNotEqual(getattr(row, 'postal_code'), original_value)
    
    def test_update_state(self):
        """ verify state (CharField) can be updated """
        row = self.bake()
        original_value = row.state
        updated_value = baker.prepare(self.to_bake, _fill_optional=['state']).state
        setattr(row, 'state', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'state'), updated_value)
        self.assertNotEqual(getattr(row, 'state'), original_value)
    
    def test_update_street_address(self):
        """ verify street_address (CharField) can be updated """
        row = self.bake()
        original_value = row.street_address
        updated_value = baker.prepare(self.to_bake, _fill_optional=['street_address']).street_address
        setattr(row, 'street_address', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'street_address'), updated_value)
        self.assertNotEqual(getattr(row, 'street_address'), original_value)
    

class AwardTests(TestCase):
    """ test CRUD operations on Award """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'award')
        self.to_bake = 'parademgr.Award'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, _fill_optional=['description', 'name'])

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_award_type(self):
        """ verify award_type (ForeignKey) can be updated """
        row = self.bake()
        original_value = row.award_type
        baker.make(self.model.award_type.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.award_type.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.award_type.field.related_model.objects.all())
        setattr(row, 'award_type', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'award_type'), updated_value)
        self.assertNotEqual(getattr(row, 'award_type'), original_value)
    
    def test_update_description(self):
        """ verify description (CharField) can be updated """
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(self.to_bake, _fill_optional=['description']).description
        setattr(row, 'description', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'description'), updated_value)
        self.assertNotEqual(getattr(row, 'description'), original_value)
    
    def test_update_division(self):
        """ verify division (ForeignKey) can be updated """
        row = self.bake()
        original_value = row.division
        baker.make(self.model.division.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.division.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.division.field.related_model.objects.all())
        setattr(row, 'division', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'division'), updated_value)
        self.assertNotEqual(getattr(row, 'division'), original_value)
    
    def test_update_name(self):
        """ verify name (CharField) can be updated """
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=['name']).name
        setattr(row, 'name', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'name'), updated_value)
        self.assertNotEqual(getattr(row, 'name'), original_value)
    

class AwardTypeTests(TestCase):
    """ test CRUD operations on AwardType """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'awardtype')
        self.to_bake = 'parademgr.AwardType'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, _fill_optional=['description'])

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_description(self):
        """ verify description (CharField) can be updated """
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(self.to_bake, _fill_optional=['description']).description
        setattr(row, 'description', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'description'), updated_value)
        self.assertNotEqual(getattr(row, 'description'), original_value)
    
    def test_update_name(self):
        """ verify name (CharField) can be updated """
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=['name']).name
        setattr(row, 'name', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'name'), updated_value)
        self.assertNotEqual(getattr(row, 'name'), original_value)
    

class CategoryTests(TestCase):
    """ test CRUD operations on Category """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'category')
        self.to_bake = 'parademgr.Category'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, _fill_optional=['description'])

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_description(self):
        """ verify description (CharField) can be updated """
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(self.to_bake, _fill_optional=['description']).description
        setattr(row, 'description', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'description'), updated_value)
        self.assertNotEqual(getattr(row, 'description'), original_value)
    
    def test_update_label(self):
        """ verify label (CharField) can be updated """
        row = self.bake()
        original_value = row.label
        updated_value = baker.prepare(self.to_bake, _fill_optional=['label']).label
        setattr(row, 'label', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'label'), updated_value)
        self.assertNotEqual(getattr(row, 'label'), original_value)
    
    def test_update_name(self):
        """ verify name (CharField) can be updated """
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=['name']).name
        setattr(row, 'name', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'name'), updated_value)
        self.assertNotEqual(getattr(row, 'name'), original_value)
    

class ContactTests(TestCase):
    """ test CRUD operations on Contact """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'contact')
        self.to_bake = 'parademgr.Contact'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, )

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_first_name(self):
        """ verify first_name (CharField) can be updated """
        row = self.bake()
        original_value = row.first_name
        updated_value = baker.prepare(self.to_bake, _fill_optional=['first_name']).first_name
        setattr(row, 'first_name', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'first_name'), updated_value)
        self.assertNotEqual(getattr(row, 'first_name'), original_value)
    
    def test_update_last_name(self):
        """ verify last_name (CharField) can be updated """
        row = self.bake()
        original_value = row.last_name
        updated_value = baker.prepare(self.to_bake, _fill_optional=['last_name']).last_name
        setattr(row, 'last_name', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'last_name'), updated_value)
        self.assertNotEqual(getattr(row, 'last_name'), original_value)
    

class DivisionTests(TestCase):
    """ test CRUD operations on Division """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'division')
        self.to_bake = 'parademgr.Division'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, _fill_optional=['description'])

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_category(self):
        """ verify category (ForeignKey) can be updated """
        row = self.bake()
        original_value = row.category
        baker.make(self.model.category.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.category.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.category.field.related_model.objects.all())
        setattr(row, 'category', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'category'), updated_value)
        self.assertNotEqual(getattr(row, 'category'), original_value)
    
    def test_update_description(self):
        """ verify description (CharField) can be updated """
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(self.to_bake, _fill_optional=['description']).description
        setattr(row, 'description', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'description'), updated_value)
        self.assertNotEqual(getattr(row, 'description'), original_value)
    
    def test_update_label(self):
        """ verify label (CharField) can be updated """
        row = self.bake()
        original_value = row.label
        updated_value = baker.prepare(self.to_bake, _fill_optional=['label']).label
        setattr(row, 'label', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'label'), updated_value)
        self.assertNotEqual(getattr(row, 'label'), original_value)
    
    def test_update_name(self):
        """ verify name (CharField) can be updated """
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=['name']).name
        setattr(row, 'name', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'name'), updated_value)
        self.assertNotEqual(getattr(row, 'name'), original_value)
    

class EmailAddressTests(TestCase):
    """ test CRUD operations on EmailAddress """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'emailaddress')
        self.to_bake = 'parademgr.EmailAddress'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, _fill_optional=['email_address_type'])

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_email(self):
        """ verify email (CharField) can be updated """
        row = self.bake()
        original_value = row.email
        updated_value = baker.prepare(self.to_bake, _fill_optional=['email']).email
        setattr(row, 'email', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'email'), updated_value)
        self.assertNotEqual(getattr(row, 'email'), original_value)
    
    def test_update_email_address_type(self):
        """ verify email_address_type (CharField) can be updated """
        row = self.bake()
        original_value = row.email_address_type
        choices = getattr(self.model.email_address_type.field, 'choices', None)
        updated_value = random.choice([i[0] for i in choices if original_value not in i])
        setattr(row, 'email_address_type', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'email_address_type'), updated_value)
        self.assertNotEqual(getattr(row, 'email_address_type'), original_value)
    

class LinkTests(TestCase):
    """ test CRUD operations on Link """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'link')
        self.to_bake = 'parademgr.Link'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, _fill_optional=['description', 'name'])

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_description(self):
        """ verify description (CharField) can be updated """
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(self.to_bake, _fill_optional=['description']).description
        setattr(row, 'description', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'description'), updated_value)
        self.assertNotEqual(getattr(row, 'description'), original_value)
    
    def test_update_name(self):
        """ verify name (CharField) can be updated """
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=['name']).name
        setattr(row, 'name', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'name'), updated_value)
        self.assertNotEqual(getattr(row, 'name'), original_value)
    
    def test_update_url(self):
        """ verify url (CharField) can be updated """
        row = self.bake()
        original_value = row.url
        updated_value = baker.prepare(self.to_bake, _fill_optional=['url']).url
        setattr(row, 'url', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'url'), updated_value)
        self.assertNotEqual(getattr(row, 'url'), original_value)
    

class OrganizationTests(TestCase):
    """ test CRUD operations on Organization """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'organization')
        self.to_bake = 'parademgr.Organization'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, _fill_optional=['description'])

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_description(self):
        """ verify description (CharField) can be updated """
        row = self.bake()
        original_value = row.description
        updated_value = baker.prepare(self.to_bake, _fill_optional=['description']).description
        setattr(row, 'description', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'description'), updated_value)
        self.assertNotEqual(getattr(row, 'description'), original_value)
    
    def test_update_name(self):
        """ verify name (CharField) can be updated """
        row = self.bake()
        original_value = row.name
        updated_value = baker.prepare(self.to_bake, _fill_optional=['name']).name
        setattr(row, 'name', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'name'), updated_value)
        self.assertNotEqual(getattr(row, 'name'), original_value)
    

class ParadeTests(TestCase):
    """ test CRUD operations on Parade """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'parade')
        self.to_bake = 'parademgr.Parade'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, _fill_optional=['title'])

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_title(self):
        """ verify title (CharField) can be updated """
        row = self.bake()
        original_value = row.title
        updated_value = baker.prepare(self.to_bake, _fill_optional=['title']).title
        setattr(row, 'title', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'title'), updated_value)
        self.assertNotEqual(getattr(row, 'title'), original_value)
    

class ParticipantTests(TestCase):
    """ test CRUD operations on Participant """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'participant')
        self.to_bake = 'parademgr.Participant'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, )

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_division(self):
        """ verify division (ForeignKey) can be updated """
        row = self.bake()
        original_value = row.division
        baker.make(self.model.division.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.division.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.division.field.related_model.objects.all())
        setattr(row, 'division', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'division'), updated_value)
        self.assertNotEqual(getattr(row, 'division'), original_value)
    
    def test_update_organization(self):
        """ verify organization (ForeignKey) can be updated """
        row = self.bake()
        original_value = row.organization
        baker.make(self.model.organization.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.organization.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.organization.field.related_model.objects.all())
        setattr(row, 'organization', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'organization'), updated_value)
        self.assertNotEqual(getattr(row, 'organization'), original_value)
    
    def test_update_parade(self):
        """ verify parade (ForeignKey) can be updated """
        row = self.bake()
        original_value = row.parade
        baker.make(self.model.parade.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.parade.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.parade.field.related_model.objects.all())
        setattr(row, 'parade', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'parade'), updated_value)
        self.assertNotEqual(getattr(row, 'parade'), original_value)
    
    def test_update_street(self):
        """ verify street (CharField) can be updated """
        row = self.bake()
        original_value = row.street
        updated_value = baker.prepare(self.to_bake, _fill_optional=['street']).street
        setattr(row, 'street', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'street'), updated_value)
        self.assertNotEqual(getattr(row, 'street'), original_value)
    

class ParticipantAwardTests(TestCase):
    """ test CRUD operations on ParticipantAward """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'participantaward')
        self.to_bake = 'parademgr.ParticipantAward'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, )

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_award(self):
        """ verify award (ForeignKey) can be updated """
        row = self.bake()
        original_value = row.award
        baker.make(self.model.award.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.award.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.award.field.related_model.objects.all())
        setattr(row, 'award', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'award'), updated_value)
        self.assertNotEqual(getattr(row, 'award'), original_value)
    
    def test_update_parade(self):
        """ verify parade (ForeignKey) can be updated """
        row = self.bake()
        original_value = row.parade
        baker.make(self.model.parade.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.parade.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.parade.field.related_model.objects.all())
        setattr(row, 'parade', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'parade'), updated_value)
        self.assertNotEqual(getattr(row, 'parade'), original_value)
    
    def test_update_winner(self):
        """ verify winner (ForeignKey) can be updated """
        row = self.bake()
        original_value = row.winner
        baker.make(self.model.winner.field.related_model._meta.label, _fill_optional=True)
        if original_value:
            updated_value = random.choice(self.model.winner.field.related_model.objects.exclude(pk=original_value.pk))
        else:
            updated_value = random.choice(self.model.winner.field.related_model.objects.all())
        setattr(row, 'winner', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'winner'), updated_value)
        self.assertNotEqual(getattr(row, 'winner'), original_value)
    

class PhoneNumberTests(TestCase):
    """ test CRUD operations on PhoneNumber """
    def setUp(self):
        self.model = apps.get_model('parademgr', 'phonenumber')
        self.to_bake = 'parademgr.PhoneNumber'

    def bake(self):
        """ add row """
        return baker.make(self.to_bake, _fill_optional=['phone_type'])

    def test_create(self):
        """ verify object can be created """
        before_count = self.model.objects.count()
        row = self.bake()
        after_count = self.model.objects.count()
        self.assertTrue(isinstance(row, self.model))
        self.assertGreater(after_count, before_count)
        
    def test_read(self):
        """ verify object can be read """
        row = self.bake()
        entry = self.model.objects.get(pk=row.pk)
        self.assertTrue(isinstance(entry, self.model))
        self.assertEqual(row.pk, entry.pk)

    def test_delete(self):
        """ verify object can be deleted """
        row = self.bake()
        before_count = self.model.objects.count()
        row_pk = row.pk
        row.delete()
        after_count = self.model.objects.count()
        with self.assertRaises(self.model.DoesNotExist):
            self.model.objects.get(pk=row_pk)
        self.assertLess(after_count, before_count)
        
    def test_update_number(self):
        """ verify number (CharField) can be updated """
        row = self.bake()
        original_value = row.number
        updated_value = baker.prepare(self.to_bake, _fill_optional=['number']).number
        setattr(row, 'number', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'number'), updated_value)
        self.assertNotEqual(getattr(row, 'number'), original_value)
    
    def test_update_phone_type(self):
        """ verify phone_type (CharField) can be updated """
        row = self.bake()
        original_value = row.phone_type
        choices = getattr(self.model.phone_type.field, 'choices', None)
        updated_value = random.choice([i[0] for i in choices if original_value not in i])
        setattr(row, 'phone_type', updated_value)
        row.save()
        self.assertEqual(getattr(row, 'phone_type'), updated_value)
        self.assertNotEqual(getattr(row, 'phone_type'), original_value)
    

