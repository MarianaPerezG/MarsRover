import sys
sys.path.append('../src')

import unittest
from rover import Rover
from planet import Planet
from main import validation_path, validation_instructions, launch_rover, validation_grid_size

class TestRover(unittest.TestCase):
	# Testing rover
	def test_turn_right(self):

		planet = Planet(2,2)
		rover = Rover(0,0,'N',planet)
		rover.turn_right()
		self.assertEqual(rover.direction, 'E')

	def test_turn_left(self):

		planet = Planet(2,2)
		rover = Rover(0,0,'N',planet)
		rover.turn_left()
		self.assertEqual(rover.direction, 'W')
		
	def test_move(self):

		planet = Planet(2,2)
		rover = Rover(0,0, 'N', planet)
		rover.move()
		self.assertEqual(rover.get_position(), [0,1])

class TestPlanet(unittest.TestCase):
	# Testing planet
	def test_build_grid(self):

		mars = Planet(2,2)
		self.assertEqual(mars.grid, [[0,0],[0,0]])

class TestValidations(unittest.TestCase):
	# Testing validation functions on the main folder
	def test_validation_of_path(self):

		self.assertTrue(validation_path('RMMMLMMLLRMMM'))
		self.assertFalse(validation_path('rmmml'))
		self.assertFalse(validation_path('R M M M'))

	def test_validation_of_instructions(self):

		self.assertTrue(validation_instructions('1 2 N'))
		self.assertFalse(validation_instructions('12N'))
		self.assertFalse(validation_instructions('12J'))

	def test_launching_of_rover(self):

		planet = Planet(2,2)
		self.assertIsInstance(launch_rover('1 2 N', planet), Rover)

	def test_validation_grid_size(self):

		self.assertTrue(validation_grid_size('2 3'))


# Para poder tener mas detalle sobre los resultados individuales de cada Test
suite_rover = unittest.TestLoader().loadTestsFromTestCase(TestRover)
suite_planet = unittest.TestLoader().loadTestsFromTestCase(TestPlanet)
suite_validations = unittest.TestLoader().loadTestsFromTestCase(TestValidations)

alltests = unittest.TestSuite((suite_rover, suite_planet, suite_validations))

unittest.TextTestRunner(verbosity=2).run(alltests)
