from unittest import TestCase
from stupid import StupidData

class A(StupidData): pass
class B(A): pass
class C:pass

class TestSubclass(TestCase):
    def test_subclass(self):
        self.assertEqual(issubclass(B, A), True)

    def test_not_subclass(self):
        self.assertEqual(issubclass(B, C), False)
