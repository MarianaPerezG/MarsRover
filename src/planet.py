from rover import Rover

class Planet(object):

	def __init__(self, x, y):

		self.height = int(y) + 1 
		self.width = int(x) + 1
		self.grid = self.build()
		self.rovers = []

	def build(self):

		# Creating a matrix that represents the grid on mars. 
		# Array of rows with 0 representig no occupied spaces and 1 the ones with a rover.
		w, h =  self.width, self.height
		return [[0 for x in range(h)] for y in range(w)] 

	def add_rover(self, rover):

		self.rovers.append(rover)

	def update_grid(self):

		for rover in self.rovers:

			position = rover.get_position()

			self.grid[position[0]][position[1]] = 1

	def paint_grid(self):

		drawn_grid = ''

		for y in range(self.height ,0, -1):

			for x in range(self.width):

				if self.grid[x][y-1] == 0:

					drawn_grid += '|   |'
				else:

					drawn_grid += '| X |'

			drawn_grid += '\n'

		print drawn_grid



# planet = Planet(5,5)
# print planet.grid
# rover = Rover(1,3, 'N', planet)
# planet.add_rover(rover)
# planet.update_grid()
# print planet.grid
# planet.paint_grid()

		




