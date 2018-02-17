class Planet(object):

	def __init__(self, x, y):

		self.height = int(y) 
		self.width = int(x)
		self.grid = self.build()

	def build(self):

		# Creating a matrix that represents the grid on mars. 
		# Array of rows with 0 representig no occupied spaces and 1 the ones with a rover.
		w, h =  self.width, self.height
		return [[0 for x in range(w)] for y in range(h)] 
		




