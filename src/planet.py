class Planet(object):

	def __init__(self, x, y):

		self.height = int(y) 
		self.width = int(x)
		self.grid = self.build()
		self.rovers = []

	def build(self):

		# Creating a matrix that represents the grid on mars. 
		# Array of rows with 0 representig no occupied spaces and 1 the ones with a rover.
		w, h =  self.width, self.height
		return [[0 for x in range(w)] for y in range(h)] 

	def add_rover(self, rover):

		self.rovers.append(rover)

	def update_grid(self):

		for rover in self.rovers:

			position = rover.get_position()

			self.grid[position[0] - 1][position[1] - 1] = 1
		




