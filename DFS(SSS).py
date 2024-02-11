class State:
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbor(self, state):
        self.neighbors.append(state)

def dfs(start_state, goal_state):
    stack = [(start_state, [])]  # Stack to keep track of states and paths

    while stack:
        current_state, path = stack.pop()  # Retrieve the current state and its path

        if current_state == goal_state:
            return path + [current_state]  # Return the path if the goal state is reached

        for neighbor in current_state.neighbors:
            if neighbor not in path:  # Avoid revisiting states already in the current path
                stack.append((neighbor, path + [current_state]))  # Add the neighbor and update the path

    return None  # Return None if no path to the goal state is found

# Example usage
# Create states
state_a = State('A')
state_b = State('B')
state_c = State('C')
state_d = State('D')
state_e = State('E')

# Define state connections
state_a.add_neighbor(state_b)
state_a.add_neighbor(state_c)
state_b.add_neighbor(state_d)
state_c.add_neighbor(state_d)
state_d.add_neighbor(state_e)

# Perform DFS
start_state = state_a
goal_state = state_e
path = dfs(start_state, goal_state)

if path:
    print("Path found:")
    for state in path:
        print(state.name)
else:
    print("No path found.")
