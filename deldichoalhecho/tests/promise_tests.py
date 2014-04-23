from django.test import TestCase
from django.utils.timezone import now
from ..models import Promise, Fulfillment
from popit.models import Person as PopitPerson, ApiInstance
from popolo.models import Person
from taggit.models import Tag

nownow = now()
class PromiseTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")

    def test_instanciate(self):
        ''' Instanciate a Promise'''
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )
        self.assertTrue(promise)
        self.assertEquals(promise.name, "this is a promise")
        self.assertEquals(promise.description, "this is a description")
        self.assertEquals(promise.date, nownow)

    def test_a_promise_has_unicode(self):
        ''' A promise has a unicode method'''
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )

        self.assertEquals(promise.__unicode__(), "A person promessed this is a promise")

    def test_a_promise_has_tags(self):
        '''A promise has tags'''
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )
        promise.tags.add('education')
        self.assertEquals(promise.tags.count(), 1)
        self.assertEquals(promise.tags.first().name,'education')


    def test_a_promise_has_one_fulfillment(self):
        '''A Promise has one fulfillment'''
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )
        promise.fulfillment.delete()
        fulfillment = Fulfillment.objects.create(promise=promise,\
                                                 percentage=100)
        self.assertEquals(promise.fulfillment, fulfillment)

    def test_a_promise_creates_one_fulfillment_automatically(self):
        '''One Promise has one fulfillment automatically'''
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )

        self.assertIsInstance(promise.fulfillment, Fulfillment)


    def test_automatically_does_not_try_to_create_two_fulfillments(self):
        '''When saving a promise does not try to create two fulfillments'''
        promise = Promise.objects.create(name="this is a promise",\
                                         description="this is a description",\
                                         date = nownow,\
                                         person = self.person
                                         )
        fulfillment = promise.fulfillment
        promise.save()
        self.assertEquals(fulfillment, promise.fulfillment)
