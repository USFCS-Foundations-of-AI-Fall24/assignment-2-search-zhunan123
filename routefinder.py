from queue import PriorityQueue
from Graph import *
from math import sqrt

class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == "1,1"


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put((0, start_state))
    previous_state = {}
    closed_list[start_state] = 0

    state_count = 0

    while not search_queue.empty():
        current_cost, current_state = search_queue.get()
        state_count += 1
        print(f"Exploring state: {current_state.location}, cost: {current_cost}")

        if goal_test(current_state):
            print(f"Total states generated: {state_count}")
            return current_state

        for edge in current_state.mars_graph.get_edges(Node(current_state.location)):
            next_node = edge.dest
            next_state = map_state(location=next_node.value, mars_graph=current_state.mars_graph,
                                   g=current_cost + edge.val, h=heuristic_fn(next_node))
            print(f"Checking neighbor {next_state.location} of {current_state.location}")
            new_cost = current_cost + edge.val
            # Check if next_state is already in the closed_list
            if next_state not in closed_list or new_cost < closed_list[next_state]:
                heuristic_cost = heuristic_fn(next_node)
                total_cost = new_cost + heuristic_cost
                search_queue.put((total_cost, next_state))
                previous_state[next_state] = current_state
                closed_list[next_state] = new_cost
                print(f"Adding state: {next_state.location} with total cost: {total_cost}")

## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    if isinstance(state, map_state):
        loc = state.location
    elif isinstance(state, Node):
        loc = state.value
    x1, y1 = map(int, loc.split(','))
    x2, y2 = (1, 1)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    mars_graph = Graph()
    node_map = {}
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        node, neighbors = line.split(':')
        node = node.strip()
        neighbors = neighbors.strip().split()
        if node not in node_map:
            current_node = Node(node)
            node_map[node] = current_node
            mars_graph.add_node(current_node)
        else:
            current_node = node_map[node]
        # Add edges for each neighbor
        for neighbor in neighbors:
            if neighbor not in node_map:
                neighbor_node = Node(neighbor)
                node_map[neighbor] = neighbor_node
                mars_graph.add_node(neighbor_node)
            else:
                neighbor_node = node_map[neighbor]
            mars_graph.add_edge(Edge(current_node, neighbor_node, 1))

    return mars_graph





