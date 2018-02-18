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

	def test_get_position(self):

		planet = Planet(2,2)
		rover = Rover(1,1,'S', planet)
		self.assertEqual(rover.get_position(), [1,1])

	def test_get_direction(self):

		planet = Planet(2,2)
		rover = Rover(1,1,'S', planet)
		self.assertEqual(rover.get_direction(), 'S')

	def test_move(self):

		planet = Planet(2,2)
		rover = Rover(0,0, 'N', planet)
		rover.move()
		self.assertEqual(rover.get_position(), [0,1])

	def test_go_back(self):

		planet = Planet(2,2)
		rover = Rover(0,1, 'N', planet)
		rover.go_back()
		self.assertEqual(rover.get_position(), [0,0])

	def test_print_status(self):

		planet = Planet(5,5)
		rover = Rover(2,3,'N', planet)
		self.assertEqual(rover.print_status(), '2 3 N')


class TestPlanet(unittest.TestCase):
	# Testing planet
	def test_build_grid(self):

		mars = Planet(2,2)
		self.assertEqual(mars.grid, [[0,0,0],[0,0,0],[0,0,0]])

	def test_add_rover(self):

		planet = Planet(2,2)
		rover = Rover(1,2,'N', planet)
		self.assertEqual(len(planet.rovers), 0)
		planet.add_rover(rover)
		self.assertEqual(len(planet.rovers), 1)

	def test_update_grid(self):

		planet = Planet(2,2)
		self.assertEqual(planet.grid[1][2], 0)
		rover = Rover(1,2,'N', planet)
		planet.add_rover(rover)
		planet.update_grid()
		self.assertEqual(planet.grid[1][2], 1)

	def test_get_rover_on_position(self):

		planet = Planet(5,5)
		rover = Rover(2,1,'N', planet)
		planet.add_rover(rover)
		planet.update_grid()

		self.assertIsInstance(planet.get_rover_on_position(2,1), Rover)
		self.assertEqual(planet.get_rover_on_position(2,1), rover)

		rover2 = Rover(3,5, 'S', planet)
		planet.add_rover(rover2)
		planet.update_grid()

		self.assertEqual(planet.get_rover_on_position(3,5), rover2)


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

		rover = Rover(1,1,'S', planet)
		planet.add_rover(rover)
		planet.update_grid()
		# send second one with same coordinates 
		self.assertFalse(launch_rover('1 1 W', planet))

	def test_validation_grid_size(self):

		self.assertTrue(validation_grid_size('2 3'))


# Para poder tener mas detalle sobre los resultados individuales de cada Test
suite_rover = unittest.TestLoader().loadTestsFromTestCase(TestRover)
suite_planet = unittest.TestLoader().loadTestsFromTestCase(TestPlanet)
suite_validations = unittest.TestLoader().loadTestsFromTestCase(TestValidations)

alltests = unittest.TestSuite((suite_rover, suite_planet, suite_validations))

unittest.TextTestRunner(verbosity=2).run(alltests)
