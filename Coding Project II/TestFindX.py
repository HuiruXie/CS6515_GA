import math
import unittest
from findX import findXinA
from GA_ProjectUtils import findX


def calls_within_acceptable_range(calls, n):
	return calls <= int(math.log(n, 2) * 2) + 2


class TestFindX(unittest.TestCase):

	def setUp(self):
		self.findX_instance = findX()

	def test_findX_with_only_one_element(self):
		x = self.findX_instance.start(1234, 1, 1)  # nLower=1, nUpper=1 guarantees a single-element array
		index, calls = findXinA(x, self.findX_instance)
		self.assertEqual(index, 1)
		self.assertTrue(calls_within_acceptable_range(calls, 1))


	def test_findX_not_in_array(self):
		x = self.findX_instance.start(2, 10, 10)
		index, calls = findXinA(x + 1, self.findX_instance)  # x + 1 is not in the array
		self.assertIsNone(index)
		self.assertTrue(calls_within_acceptable_range(calls, 10))

	def test_findX_in_large_array(self):
		x = self.findX_instance.start(3, 10000, 10000)
		index, calls = findXinA(x, self.findX_instance)
		self.assertIsNotNone(index)
		self.assertTrue(calls_within_acceptable_range(calls, 10000))

	def test_findX_very_large_array(self):
		x = self.findX_instance.start(5, 1000000, 1000000)  # Very large array
		index, calls = findXinA(x, self.findX_instance)
		self.assertIsNotNone(index)
		self.assertTrue(calls_within_acceptable_range(calls, 1000000))

	def test_findX_very_very_large_array(self):
		x = self.findX_instance.start(5, 10000000, 10000000)
		index, calls = findXinA(x, self.findX_instance)
		self.assertIsNotNone(index)
		self.assertTrue(calls_within_acceptable_range(calls, 10000000))

	def test_findX_with_different_seeds(self):
		for seed in range(1, 1000):
			x = self.findX_instance.start(seed)
			index, calls = findXinA(x, self.findX_instance)
			self.assertIsNotNone(index)
	def test_findX_with_static_seed(self):
		for i in range(1, 10000):
			x = self.findX_instance.start(22222, 1, i)
			index, calls = findXinA(x, self.findX_instance)
			self.assertIsNotNone(index)

	def test_findX_defined_arr_lengths(self):
		for seed in range(1, 10000):
			x = self.findX_instance.start(seed, seed, seed)
			index, calls = findXinA(x, self.findX_instance)
			self.assertIsNotNone(index)
			self.assertTrue(calls_within_acceptable_range(calls, seed))


if __name__ == '__main__':
	unittest.main()
