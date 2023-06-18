from unittest import TestCase
from facility import Facility
from sensor import Sensor


class TestFunctions(TestCase):
    def test_factory(self):
        s = Sensor('test', 1, 0)

        f = Facility('testf1', s)

        self.assertEqual(f.sensor[0], s)
        self.assertFalse(1)


test = TestFunctions().test_factory()
