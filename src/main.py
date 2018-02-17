from rover import Rover
from planet import Planet

def move_rover(path):

	# Function for movement of the rover following path
	print 'MOVE'

def launch_rover(instructions):

	instuctions = instructions.split(' ')

	return Rover(instructions[0], instructions[1], instructions[2])

# Validation for the creation of the Planet instance
def validation_grid_size(grid_size):

	try:
		array = grid_size.split(' ')

		if len(array) == 2:

			try:
				if int(array[0]) > 0  and int(array[1]):

					return True
			except:

				return False
		else:

			return False

	except Exception,e:

		return False

# Validation for the creation of the Rover instance
def validation_path(path):

	try:
		for i in range(len(path) -1):

			if path[i] not in ['M', 'L', 'R']:

				return False

		return True

	except Exception, e:
		return False

def validation_instructions(instructions):

	try:
		array = instructions.split(' ')

		if len(array) == 3 and array[2] in ['N', 'E', 'S', 'W']:
			return True
		else:
			return False

	except Exception, e:
		return False


def main():

	# Opening the file input.txt with the instructions
	with open('input.txt') as input_text:

		content = input_text.readlines()
		content = [result.strip() for result in content]

	# Grid size received from input
	grid_size = content[0]

	# Creating the planet
	if validation_grid_size(grid_size):

		mars = Planet(grid_size[0], grid_size[2])

	else:
		print 'Size of grid given is incorrect'

	# Launch every rover on the instructions read before
	for i in range(1,len(content),2):

		initiation_instructions = content[i]
		rover_path = content[i+1]

		if validation_instructions(initiation_instructions):
		
			rover = launch_rover(initiation_instructions)

			if validation_path(rover_path):

				move_rover(rover_path)

			else:
				print 'Path given for the movement of rover is incorrect'

		else:
			print 'Instructions given for rover launching are incorrect'


if __name__ == "__main__":
    main()