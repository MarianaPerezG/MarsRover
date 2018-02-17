directions = ['N', 'E', 'S', 'W']

class Rover(object):

	def __init__(self, x, y, direction, planet):

		self.position_x = int(x)
		self.position_y = int(y)
		self.direction = direction
		self.planet = planet

	def move(self):

		if self.direction == 'N':
			self.position_y += 1
		elif self.direction == 'E':
			self.position_x += 1 
		elif self.direction == 'S':
			self.position_y -= 1
		elif self.direction == 'W':
			self.position_x -= 1

		# Checking if the move can be made
		if self.planet.grid[self.get_position()[0] -1][self.get_position()[1] -1] == 1:
			self.go_back()
		else:
			return True

	def go_back(self):

		if self.direction == 'N':
			self.position_y -= 1
		elif self.direction == 'E':
			self.position_x -= 1 
		elif self.direction == 'S':
			self.position_y += 1
		elif self.direction == 'W':
			self.position_x += 1

	def turn_right(self):

		index = directions.index(self.direction)

		self.direction = 'N' if index == 3 else directions[index + 1]

	def turn_left(self):

		index = directions.index(self.direction)

		self.direction = 'W' if index == 0 else  directions[index - 1]

	def get_position(self):

		return [self.position_x, self.position_y]

	def print_status(self):

		return "{} {} {}".format(self.position_x, self.position_y, self.direction)

