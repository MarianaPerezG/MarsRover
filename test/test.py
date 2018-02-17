import sys
sys.path.append('../src')

import unittest
from rover import Rover
from planet import Planet

class TestRover(unittest.TestCase):
	# Testing rover
	def test_turn_right(self):

		rover = Rover(0,0,'N')
		rover.turn_right()
		self.assertEqual(rover.direction, 'E')

	def test_turn_left(self):

		rover = Rover(0,0,'N')
		rover.turn_left()
		self.assertEqual(rover.direction, 'W')
		
	def test_move(self):

		rover = Rover(0,0, 'N')
		rover.move()
		self.assertEqual(rover.get_position(), [0,1])

class TestPlanet(unittest.TestCase):
	# Testing planet
	def test_build_grid(self):

		mars = Planet(2,2)
		self.assertEqual(mars.grid, [[0,0],[0,0]])


# Para poder tener mas detalle sobre los resultados individuales de cada Test
suite_rover = unittest.TestLoader().loadTestsFromTestCase(TestRover)
suite_planet = unittest.TestLoader().loadTestsFromTestCase(TestPlanet)

alltests = unittest.TestSuite((suite_rover, suite_planet))

unittest.TextTestRunner(verbosity=2).run(alltests)
