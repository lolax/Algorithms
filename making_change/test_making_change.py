import unittest
from making_change import making_change 

class Test(unittest.TestCase):

  def setUp(self):
    self.denominations = [1, 5, 10, 25, 50]

  def test_making_change_small_amount(self):
    self.assertEqual(making_change(0, [1, 5, 10, 25, 50]), 1)
    self.assertEqual(making_change(1, [1, 5, 10, 25, 50]), 1)
    self.assertEqual(making_change(5, [1, 5, 10, 25, 50]), 2)
    self.assertEqual(making_change(10, [1, 5, 10, 25, 50]), 4)
    self.assertEqual(making_change(20, [1, 5, 10, 25, 50]), 9)
    self.assertEqual(making_change(30, [1, 5, 10, 25, 50]), 18)
    self.assertEqual(making_change(100, [1, 5, 10, 25, 50]), 292)
    self.assertEqual(making_change(200, [1, 5, 10, 25, 50]), 2435)
    self.assertEqual(making_change(300, [1, 5, 10, 25, 50]), 9590)

  def test_making_change_large_amount(self):
    self.assertEqual(making_change(350, [1, 5, 10, 25, 50]), 16472)
    self.assertEqual(making_change(400, [1, 5, 10, 25, 50]), 26517)
    self.assertEqual(making_change(1000, [1, 5, 10, 25, 50]), 801451)
    self.assertEqual(making_change(2000, [1, 5, 10, 25, 50]), 11712101)
    self.assertEqual(making_change(5000, [1, 5, 10, 25, 50]), 432699251)
    self.assertEqual(making_change(10000, [1, 5, 10, 25, 50]), 6794128501)


if __name__ == '__main__':
  unittest.main()