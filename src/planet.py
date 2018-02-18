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

					rover = self.get_rover_on_position(x,y-1)

					string = '| {} |'

					rover_direction = rover.get_direction() 

					if rover_direction == 'N':

						char = '^'

					elif rover_direction == 'E':

						char = '>'

					elif rover_direction == 'S':
						
						char = 'v'

					else:

						char = '<'

					drawn_grid += string.format(char)


			drawn_grid += '\n'

		print drawn_grid

	def get_rover_on_position(self, x, y):

		for rover in self.rovers:

			position = rover.get_position()
		
			if position[0] == x and position[1] == y:

				return rover 

		return False









		




