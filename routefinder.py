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
        return self.location == '0,0' # change from '1,1'


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put((0, start_state))
    previous_state = {}
    closed_list[start_state] = 0

    while not search_queue.empty():
        current_cost, current_state = search_queue.get()
        if goal_test(current_state):
            return current_state
        if use_closed_list and current_state in closed_list:
            continue

        for edge in current_state.mars_graph.get_edges(current_state):
            next_state = edge.dest
            new_cost = closed_list[current_state] + edge.val
            if next_state not in closed_list or new_cost < closed_list[next_state]:
                closed_list[next_state] = new_cost
                cost = new_cost + heuristic_fn(next_state)
                search_queue.put((cost, next_state))
                previous_state[next_state] = current_state




## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    x1, y1 = map(int, state.location.split(','))
    x2, y2 = (0, 0)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    mars_graph = Graph()

    with open(filename, 'r') as f:
        rows = f.readlines()

    row_count = len(rows)
    col_count = len(rows[0].strip().split(','))

    i = 0
    while i < row_count:
        row = rows[i].strip()
        cols = row.split(',')
        j = 0
        while j < col_count:
            cell = cols[j].strip()
            if cell == 'Charger':
                charger_position = Node(f"{i},{j}")
                mars_graph.add_node(charger_position)
            elif cell == 'Samples':
                samples_position = Node(f"{i},{j}")
                mars_graph.add_node(samples_position)
            elif cell != 'red':
                current_node = Node(f"{i},{j}")
                mars_graph.add_node(current_node)
                # up cell
                if i > 0 and rows[i - 1].strip().split(',')[j] != 'red':
                    up_node = Node(f"{i - 1},{j}")
                    mars_graph.add_edge(Edge(current_node, up_node, 1))
                # down cell
                if i < row_count - 1 and rows[i + 1].strip().split(',')[j] != 'red':
                    down_node = Node(f"{i + 1},{j}")
                    mars_graph.add_edge(Edge(current_node, down_node, 1))
                # left cell
                if j > 0 and cols[j - 1] != 'red':
                    left_node = Node(f"{i},{j - 1}")
                    mars_graph.add_edge(Edge(current_node, left_node, 1))
                # right cell
                if j < col_count - 1 and cols[j + 1] != 'red':
                    right_node = Node(f"{i},{j + 1}")
                    mars_graph.add_edge(Edge(current_node, right_node, 1))
            j += 1
        i += 1
    return mars_graph





