from unittest import TestCase
from routefinder import *

class Testmap_state(TestCase):
    mars_graph = None

    @classmethod
    def setUpClass(cls):
        cls.mars_graph = read_mars_graph('marsmap.txt')

        print("Checking neighbors for 2,4:")
        for edge in cls.mars_graph.get_edges(Node("2,4")):
            print(f"2,4 -> {edge.dest}")


    def test_is_lt (self) :
        s1 = map_state(g = 1,h=1)
        s2 = map_state(g=2,h=2)
        print(s1 < s2)
        self.assertLessEqual(s1,s2)


    def test_sld(self) :
        s1 = map_state(location="2,3", mars_graph=self.mars_graph, g = 1,h=1)
        val = sld(s1)
        self.assertLessEqual(val, 14)

    def test_uniform_cost_search(self):
        start_state = map_state(location="7,7", mars_graph=self.mars_graph)
        goal_state = a_star(start_state, heuristic_fn=h1, goal_test=lambda s: s.is_goal(),use_closed_list=True)
        self.assertIsNotNone(goal_state)
        self.assertTrue(goal_state.is_goal())

    def test_astar(self):
        start_state = map_state(location="7,7", mars_graph=self.mars_graph)
        goal_state = a_star(start_state, heuristic_fn=sld, goal_test=lambda s: s.is_goal())
        self.assertIsNotNone(goal_state)
        self.assertTrue(goal_state.is_goal())
