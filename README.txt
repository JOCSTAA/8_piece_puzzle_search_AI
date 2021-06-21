STUDENT NAME : CHIBUIKE JOSHUA OGBONDA
STUDENT ID: T987K298

Entire assignment is on the T987k298.py program, run on any computer with python installed

-program reads start state data from the user element by element(only values from 0 - 8 are accepted into the array and repitition of values is obsereved and corrected)
-program read goal state data from the user similar to start state.
-program calculate the steps necessary to go from start to goal state using the A*search( where f(n) = g(n) + h(n))
	-g(n)= number of nodes visited in each step
	-h(n)= heuristic function(manhattan distance) = summation for all elements in start node: abs(goal[i]-start[i]) + abs(goal[j]-start[j]), assuming array is start[i;0-3][j;0-3]

-program output the steps taken to reach goal state and the respective step number as tittle
	example:STEP 1
		3  1  2
		6  4  5
		7  0  8

		STEP 2
		3  1  2
		6  4  5
		0  7  8

		.
		.
		.

		STEP 4
		0  1  2
		3  4  5
		6  7  8

- time taken to go from a certain state to goal state is approximately b^(d+1)
	with b being the branching factor : approx 3
	and d being the depth required from start to goal

- certain states cannot be reached from a given start states
	during such outcomes program keeps running until frontier is empty

-certain states requires too much lot of time to be reached 
	for example at d = 12, time taken would be approx 3^13 = 1594323*time for one step

program can be closed manually if solution is found

THANK YOU!