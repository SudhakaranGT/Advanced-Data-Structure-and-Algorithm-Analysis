
def bfs(start_state, goal_state, successors_fn):
    visited = set()  # Set to store visited states
    queue = deque([(start_state, [])])  # Queue to store states to be explored
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path  # Return the path if goal state is reached
        
        visited.add(current_state)
        
        # Generate successor states
        successors = successors_fn(current_state)
        
        for successor in successors:
            if successor not in visited:
                queue.append((successor, path + [successor]))
    
    return None  # Return None if no path to the goal state is found

# Example usage
def successors_fn(state):
    # Define the successor function for your problem
    # It should generate and return the successor states of the current state
    
    # Example: Assuming the state is represented as a string of digits,
    # the successor function can generate all possible states by adding 1 to each digit
    
    successors = []
    for i in range(len(state)):
        digit = int(state[i])
        new_digit = (digit + 1) % 10  # Wrap around to 0 if digit is 9
        new_state = state[:i] + str(new_digit) + state[i+1:]
        successors.append(new_state)
    
    return successors

start_state = "000"
goal_state = "321"

path = bfs(start_state, goal_state, successors_fn)

if path is None:
    print("No path to the goal state found.")
else:
    print("Path to the goal state:", path)
