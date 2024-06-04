from unittest import TestCase, main
from unittest.mock import MagicMock
from ex_01_real_object import RealObject


real = RealObject()

real.get_param = MagicMock(return_value="param")


class TestParam(TestCase):
    
    def test_return_value(self):
        self.assertEqual(real.get_param(), "param")


if __name__ == '__main__':
    main()