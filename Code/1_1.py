# Initial variables
NUM_POINTS = 100
BACKWARDS_DIRECTION = "L"
GOAL_NUMBER = 0
password = 0
position = 50

# Open file with input
input_file = open("Inputs/1_1.txt")

# Get input and turn it into strings
input_content = input_file.read()

turns = input_content.split("\n")

for turn in turns:
	# Split turn into direction and rotation
	direction = turn[0]
	rotation = int(turn[1:])

	# Reverse rotation if going backwards
	if(direction==BACKWARDS_DIRECTION):
		rotation*=-1

	# Rotate position
	position+=rotation

	# Constrain position to total points
	position%=NUM_POINTS

	# Check if we're at goal number and increment password if so
	if(position==GOAL_NUMBER):
		password+=1

print(password)