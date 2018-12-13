import unittest
from mathfunc import *


class TestMathFunc(unittest.TestCase):
    '''
    skip装饰器一共有三个
    unittest,skip(reason)：无条件跳过
    unittest.skipIf(condition, reason)：当condition为True时跳过
    unittest.skipUnless(condition, reason)：当condition为False时跳过
    '''
    @unittest.skip("i don't want to run this case.")
    def test_add(self):
        self.assertEqual(3, add(1, 2))
        self.assertNotEqual(3, add(2, 2))

    def test_minus(self):
        self.assertEqual(1, minus(3, 2))

    def test_multi(self):
        self.assertEqual(6, multi(3, 2))

    def test_divide(self):
        self.assertEqual(2, divide(6, 3))
        self.assertEqual(2, divide(5, 2))


if __name__ == '__main__':
    unittest.main()
