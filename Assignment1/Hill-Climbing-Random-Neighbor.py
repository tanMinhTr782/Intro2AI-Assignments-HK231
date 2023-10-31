from random import randint
import psutil
import timeit
global N
# Randomly generate N queens in N places, in the board
# State: rows where the queen is placed.
# Board: Contains the sample board with n-queen placed in each column to test. 
def initRandomState(board, state): 
	for i in range(N): 

		# Get random row index 
		state[i] = randint(0, 100000) % N 

		# Placing a queen on board on the random row obtained before . 
		board[state[i]][i] = 1

def printBoard(board): 
	
	for i in range(N): 
		print(*board[i])  
# Fill the board with a specific value
def fill (board,value): 
	for i in range(N): 
		for j in range(N): 
			board[i][j] = value

# Generate the board with new order of N-queens (in the "state" array) 
def genBoard(board,state): 
	fill(board, 0) 
	for i in range(N): 
		board[state[i]][i] = 1
# Function to copy value between array. 
def copyValueBetweenState(state1, state2): 
	for i in range(N): 
		state1[i] = state2[i]

def compareStates(state1, state2): 
	for i in range(N): 
		if state1[i] != state2[i]: 
			return False
	return True

#Calculate how many queens got attacked (heuristic function). 
def calObjectiveVal( board, state): 

	# For each queen in a column, check if others queens 
	# are in the attack zone of this queen (Up, Down, Left/Right Diagonals)
	# If exist, ++Number of queens attack each other.

	# Number of queens attack each other,  
	queensAttacked = 0

	for i in range(N): 

		# At each column 'i', the queen is placed at row 'state[i]'

		# Check leftside of the same row (rowIdx = const colIdx decrease) 
		row = state[i] 
		col = i - 1
		
		#if Found the queen that can be attacked, break the loop. 
		while (col >= 0 and board[row][col] != 1): 
			col = col - 1
		
		if (col >= 0 and board[row][col] == 1): 
			queensAttacked = queensAttacked + 1 
		
		# Check rightSide of the same row (rowIdx = const colIdx decrease) 
		row = state[i] 
		col = i + 1

		#if Found the queen that can be attacked, break the loop. 
		while (col < N and board[row][col] != 1): 
			col = col + 1 
		
		if (col < N and board[row][col] == 1): 
			queensAttacked = queensAttacked + 1
		
		# Check leftUp Diagonal of the same row (rowIdx & colIdx decrease) 
		row = state[i] - 1
		col = i - 1
		
		#if Found the queen that can be attacked, break the loop. 
		while (col >= 0 and row >= 0 and board[row][col] != 1): 
			col = col - 1 
			row = row - 1 

		if (col >= 0 and row >= 0 and board[row][col] == 1): 
			queensAttacked = queensAttacked + 1
		

		# Check rightUp Diagonal of the same row (rowIdx & colIdx increase) 
		row = state[i] + 1
		col = i + 1

		while (col < N and row < N and board[row][col] != 1): 
			col = col + 1 
			row = row + 1  
		

		if (col < N and row < N and board[row][col] == 1): 
			queensAttacked += 1 
		
		# Check leftDown Diagonal of the same row (rowIdx inc & colIdx dec)
		row = state[i] + 1
		col = i - 1
		while (col >= 0 and row < N and board[row][col] != 1): 
			col = col - 1 
			row = row + 1  
		
		if (col >= 0 and row < N and board[row][col] == 1): 
			queensAttacked += 1 
		
		# Check rightDown Diagonal of the same row (rowIdx dec & colIdx inc) 

		row = state[i] - 1
		col = i + 1
		while (col < N and row >= 0 and board[row][col] != 1): 
			col = col + 1  
			row = row - 1 
		
		if (col < N and row >= 0 and board[row][col] == 1): 
			queensAttacked = queensAttacked + 1
		
	 
	return queensAttacked 

def getNeighbour(board, state): 

	optimalBoard = [[0 for i in range(N)] for i in range(N)] 
	optimalState = [0 for i in range(N)] 

	# Decl & Init the optimal board by the current board. 
	copyValueBetweenState(optimalState, state) 
	genBoard(optimalBoard, optimalState) 

	# Init the optimal objective value
	optimalObjectiveVal = calObjectiveVal(optimalBoard, optimalState) 

	Neighbour_Board = [[0 for i in range(N)] for i in range(N)] 
	
	Neighbour_State = [0 for i in range(N)] 
	
	# Decl & init the temporary board and state for calcualate. 
	copyValueBetweenState(Neighbour_State, state) 
	genBoard(Neighbour_Board, Neighbour_State) 

	# Try all possible neighbours of current board. 
	for i in range(N): 
		for j in range(N): 

			# Condition to skip the current state for exploring the neighbors
			if (j != state[i]): 

				# Init temp neighbour with current neighbour. 
				Neighbour_State[i] = j 
				Neighbour_Board[Neighbour_State[i]][i] = 1 
				Neighbour_Board[state[i]][i] = 0 

				# Calculate objective value of the neighbour. 
				temp = calObjectiveVal( Neighbour_Board, Neighbour_State) 

				# Compare objectives val between temporary vs optimalNeighbour
				# if temporary <= optimalNeighbour -> Update optimalNeighbour.

				if (temp <= optimalObjectiveVal) : 
					optimalObjectiveVal = temp 
					copyValueBetweenState(optimalState, Neighbour_State) 
					genBoard(optimalBoard, optimalState) 
				
				# Going back to the currentBoard for the next iteration. 
				Neighbour_Board[Neighbour_State[i]][i] = 0 
				Neighbour_State[i] = state[i] 
				Neighbour_Board[state[i]][i] = 1 
			
	# Assign the optimal board and its state to the current board and state. 
	copyValueBetweenState(state, optimalState) 
	fill(board, 0) 
	genBoard(board, state) 

	
def hillClimbing(board, state): 
# Decl & init Neighbour_Board and its state with the current Board & state . 
 

	Neighbour_Board = [[0 for i in range(N)] for i in range(N)] 
	Neighbour_State = [0 for i in range(N)] 

	copyValueBetweenState(Neighbour_State, state) 
	genBoard(Neighbour_Board, Neighbour_State) 
	
	while True: 

		# Copy state & board of Neigbour to current board, since currentBoard become its neighbour after jump. 

		copyValueBetweenState(state, Neighbour_State) 
		genBoard(board, state) 

		# Find the optimal Neigbour to jump. 

		getNeighbour(Neighbour_Board, Neighbour_State) 

		# If neighbour and current are equal -> No more optimal neighbour exist -> print result and break the loop.  
		
		if (compareStates(state, Neighbour_State)): 

			printBoard(board) 
			break 
		# If Neighbour_State != currentState, but objective are equals -> Approach a shoulder or local optimum 
		# -> Jump to a random neighbour to escape.  
		elif (calObjectiveVal(board, state) == calObjectiveVal( Neighbour_Board,Neighbour_State)): 

			# Random neighbour 
			Neighbour_State[randint(0, 100000) % N] = randint(0, 100000) % N 
			genBoard(Neighbour_Board, Neighbour_State) 

# Driver code
initial_memory = psutil.Process().memory_info().rss

N = input("Enter the number of Queens :")
N = int(N)

startTime = timeit.default_timer()

state = [0] * N 
board = [[0 for i in range(N)] for i in range(N)] 

# Init a starting board, contains N-queens randomly.  
initRandomState(board, state) 

# Apply hill Climbing on the board obtained. 

hillClimbing(board, state) 
endTime = timeit.default_timer()
    # Get the final memory usage

final_memory = psutil.Process().memory_info().rss

    # Calculate the total memory usage
total_memory = final_memory - initial_memory

print("Total memory usage:", total_memory, "bytes")
 
print("Time elapsed:", (endTime - startTime) * 1000, "ms")
