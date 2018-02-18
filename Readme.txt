RUNNING INSTRUCTIONS

For the initialization of the program use the terminal and from the root of the project use the command python /src/main.py

For the running of the testing file use the command python /test/test.py once again from the root of the project.

As for evidence on the correct functioning of the code, I’ve included a video simulation of a session on the terminal running the tests and the code with the default input.txt file.

—————————————————————————————————————————

EXPLANATION OF CODE STRUCTURE

I’ve decided to create two main clases, Planet and Rover, a main function handling the flow, and small methods for validations and reusable tasks.

The Planet class handles everything to do with the creation, building of inside grid, updating of grid and displaying of the final map from the positions occupied by the rovers. The planet will storage a collection of rover instances associated to it for occupied spaces managing. 

The Rover class handles the turning and moving tasks of itself and provides information about current position and direction. As a initialization parameter it will receive the planet(instance) in with it’ll move.

For the main function, it handles the flow of the application and calls the different validation and tasks as necessary.

The main folder is separated in src and test.The src folder containing the rover.py file with the Rover class, the planet.py file with the Planet class and the main.py file with the main function and complementary ones. On the src folder also a file input.txt as be used as the default .txt file for the input instructions.On the test folder, a test.py file with all the tests.

—————————————————————————————————————————

CODE FLOW

1.The main function will read the instruction for the path to the file with the input, retrieving the grid size and the instructions for the rovers initialization.
 
2.It’ll validate the grid size and instantiate the planet. 

3.For the rest part of the content of the file, it’ll separate the lines in sets of two, announcing the number of rovers about to be launched.

4.The rovers will be launched one by one validating the first line of instruction as the instantiating attributes and will create a new object(rover).

5.Once the rover is successfully initialized, it’ll be added to the planet.

6.The next line of the content, associated to the path the rover has to follow, will be validated and the rover will be given the instructions for movement.

7.The rover instance will be responsable of checking if the move is posible and execute it.

8. Once the movements are made, the main function is the responsible for showing the output as a message, either indicating the successful movement of the rover through the path or announcing the final position of the rover as it couldn’t continue its journey. 

9.The planet grid will be updated with the final position of the rover that just finished. 

10.Once all rovers finished their movements, the planet will display the final grid indicating empty spaces and spaces filled with a rover showing their direction.


—————————————————————————————————————————-

ASSUMPTIONS MADE

- When a rover finds a space on the grid that is occupied it stays and terminates its movements. 

- The initial instruction will ask the path to the file with the input until it’s a valid path or it’s blank so it uses the default one. 

- The format of the input file will always have the first line dedicated to the grid size and two by two the instructions for the rover initializing and movement.

- If the initial position where the rover is supossed to be launched are occupied by another rover, it will not be launched and a warning will be shown.

