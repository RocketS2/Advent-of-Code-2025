from math import floor

# Initial variables
NUM_POINTS = 100
BACKWARDS_DIRECTION = "L"
GOAL_NUMBER = 0
password = 0
position = 50

# Open file with input
input_file = open("Inputs/1_2.txt")

# Get input and turn it into strings
input_content = input_file.read()

turns = input_content.split("\n")

for turn in turns:
	# Split turn into direction and rotation
	direction = turn[0]
	rotation = int(turn[1:])
	turning_backwards = direction==BACKWARDS_DIRECTION

	# Check if the goal's going to be passed
	distance_to_goal = GOAL_NUMBER-position

	if(turning_backwards):
		distance_to_goal*=-1

	distance_to_goal = distance_to_goal%NUM_POINTS
	distance = rotation%NUM_POINTS # Constrained to prevent big turns from counting

	if(distance>distance_to_goal and distance_to_goal>0):
		password+=1

	# Add each full rotation around (since that'd have to include the goal number)
	password+=floor(rotation/NUM_POINTS)

	# Reverse rotation if going backwards
	if(turning_backwards):
		rotation*=-1

	# Rotate position
	position+=rotation

	# Constrain position to total points
	position%=NUM_POINTS

	# Check if we're at goal number and increment password if so
	if(position==GOAL_NUMBER):
		password+=1

print(password)