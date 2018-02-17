directions = ['N', 'E', 'S', 'W']

class Rover(object):

	def __init__(self, x, y, direction):

		self.position_x = x
		self.position_y = y
		self.direction = direction

	def move(self):

		if self.direction == 'N':
			self.position_y += 1
		elif self.direction == 'E':
			self.position_x += 1 
		elif self.direction == 'S':
			self.position_y -= 1
		elif self.direction == 'W':
			self.position_x -= 1

	def turn_right(self):

		index = directions.index(self.direction)

		self.direction = 'N' if index == 3 else directions[index + 1]

	def turn_left(self):

		index = directions.index(self.direction)

		self.direction = 'W' if index == 0 else  directions[index - 1]

	def get_position(self):

		return [self.position_x, self.position_y]

