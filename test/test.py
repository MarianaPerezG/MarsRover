import sys
sys.path.append('../src')

import unittest
from rover import Rover
class TestRover(unittest.TestCase):
	# Testing rover function for turning right
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


# Para poder tener mas detalle sobre los resultados individuales de cada Test
suite = unittest.TestLoader().loadTestsFromTestCase(TestRover)
unittest.TextTestRunner(verbosity=2).run(suite)
