from unittest import TestCase
from dataclasses import is_dataclass
from stupid import StupidData

class User(StupidData):
    name: str
    foo: bool = True

class AccessData(StupidData):
    access_code: str

class ApiPayload(User, AccessData):
    pass

class TestDataclass(TestCase):
    def test_slots(self):
        self.assertIn('name', ApiPayload.__slots__)
        self.assertIn('access_code', ApiPayload.__slots__)

    def test_init_works(self):
        payload = ApiPayload(name="root", access_code='test_access_code')
        self.assertEqual('root', payload.name)
        self.assertEqual('test_access_code', payload.access_code)
        self.assertTrue(payload.foo)

    def test_init_raises_when_params_missing(self):
        with self.assertRaises(TypeError):
            payload = ApiPayload()

    def test_assign_works(self):
        payload = ApiPayload(name="root", access_code='test_access_code')
        payload.name = 'not_root'
        self.assertEqual('not_root', payload.name)

    def test_assign_raises_when_not_defined(self):
        payload = ApiPayload(name="root", access_code='test_access_code')
        with self.assertRaises(AttributeError):
            payload.extra = 1

    def test_is_dataclass(self):
        self.assertTrue(is_dataclass(ApiPayload))
