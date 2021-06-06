from unittest import TestCase
from stupid import StupidData

class User(StupidData):
    name: str

class AccessData(StupidData):
    access_code: str

class ApiPayload(User, AccessData):
    pass

class NotPartOfMRO:
    pass

class TestIsInstance(TestCase):
    def setUp(self):
        self.payload = ApiPayload(name="root", access_code='test_access_code')

    def test_isinstance(self):
        self.assertTrue(isinstance(self.payload, User))
        self.assertTrue(isinstance(self.payload, AccessData))
        self.assertTrue(isinstance(self.payload, ApiPayload))
        self.assertTrue(isinstance(self.payload, (User, AccessData)))
        self.assertTrue(isinstance(self.payload, (User, AccessData, ApiPayload)))
        self.assertTrue(isinstance(self.payload, (User, AccessData, ApiPayload, NotPartOfMRO)))

    def test_not_isinstance(self):
        self.assertFalse(isinstance(self.payload, (NotPartOfMRO, )))
