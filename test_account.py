import unittest
from account import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.a1 = Account('account1')
        self.a2 = Account('account2')


    def tearDown(self) -> None:
        del self.a1
        del self.a2

    def test_init(self):
        self.assertEqual(self.a1.get_balance(), 0)
        self.assertEqual(self.a2.get_balance(), 0)
        self.assertEqual(self.a1.get_name(), 'account1')
        self.assertEqual(self.a2.get_name(), 'account2')


    def test_deposit(self):
        self.assertTrue(self.a1.deposit(2112))
        self.assertTrue(self.a2.deposit(211280))
        self.assertEqual(self.a1.get_balance(), 2112)
        self.assertEqual(self.a2.get_balance(), 211280)
        self.assertFalse(self.a1.deposit(0))
        self.assertFalse(self.a1.deposit(-80))
        self.assertFalse(self.a2.deposit(0))
        self.assertFalse(self.a2.deposit(-2112))


    def test_withdraw(self):
        self.a1.deposit(2112)
        self.a2.deposit(80)
        self.assertTrue(self.a1.withdraw(80))
        self.assertTrue(self.a2.withdraw(40))
        self.assertEqual(self.a1.get_balance(), 2032)
        self.assertEqual(self.a2.get_balance(), 40)
        self.assertFalse(self.a1.withdraw(-2112))
        self.assertFalse(self.a1.withdraw(0))
        self.assertFalse(self.a2.withdraw(-80))
        self.assertFalse(self.a2.withdraw(0))


if __name__ == '__main__':
    unittest.main()
