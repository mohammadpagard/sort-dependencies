from unittest import TestCase
import solution


class SolutionTests(TestCase):
	packages = {
		'pkg1': ['pkg3'], 'pkg2':['pkg3'], 'pkg3': [], 'pkg4':['pkg1', 'pkg2']
	}

	def test_pkg1(self):
		self.assertEqual(
			solution.sort_dependencies(self.packages, 'pkg1'),
			['pkg3']
		)

	def test_pkg2(self):
		self.assertEqual(
			solution.sort_dependencies(self.packages, 'pkg2'),
			['pkg3']
		)

	def test_pkg3(self):
		self.assertEqual(
			solution.sort_dependencies(self.packages, 'pkg3'),
			[]
		)

	def test_pkg4(self):
		self.assertEqual(
			solution.sort_dependencies(self.packages, 'pkg4'),
			['pkg3', 'pkg2', 'pkg1']
		)
