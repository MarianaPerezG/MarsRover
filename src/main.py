from rover import Rover

def move_rover(path):

	# Function for movement of the rover following path
	print 'MOVE'

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


def launch_rover(instructions):

	instuctions = instructions.split(' ')

	return Rover(instructions[0], instructions[1], instructions[2])


def main():

	# Opening the file input.txt with the instructions
	with open('input.txt') as input_text:

		content = input_text.readlines()
		content = [result.strip() for result in content]

	# Launch every rover on the instructions read before
	for i in range(1,len(content),2):

		instructions = content[i]
		path = content[i+1]

		if validation_instructions(instructions):
		
			rover = launch_rover(instructions)

			if validation_path(path):

				move_rover(path)

			else:
				print 'Path given to move rover in incorrect'

		else:
			print 'Instructions given for rover launching are incorrect'


if __name__ == "__main__":
    main()