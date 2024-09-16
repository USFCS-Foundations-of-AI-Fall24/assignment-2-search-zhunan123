from unittest import TestCase
from routefinder import *

class Testmap_state(TestCase):
    mars_graph = None

    @classmethod
    def setUpClass(cls):
        cls.mars_graph = read_mars_graph('mars_map.txt')

        print("Checking neighbors for 1,2:")
        for edge in cls.mars_graph.get_edges(Node("1,2")):
            print(f"1,2 -> {edge.dest}")


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
        start_state = map_state(location="8,8", mars_graph=self.mars_graph)
        goal_state = a_star(start_state, heuristic_fn=h1, goal_test=lambda s: s.is_goal(),use_closed_list=True)
        self.assertIsNotNone(goal_state)
        self.assertTrue(goal_state.is_goal())

    def test_astar(self):
        start_state = map_state(location="8,8", mars_graph=self.mars_graph)
        goal_state = a_star(start_state, heuristic_fn=sld, goal_test=lambda s: s.is_goal())
        self.assertIsNotNone(goal_state)
        self.assertTrue(goal_state.is_goal())

        '''
            incorrect result:
                Exploring state: 2,2, cost: 0
                No neighbors found for state 2,2. Path is blocked.
                Goal not reachable from 2,2. Exiting.
            correct result:
                Exploring state: 8,8, cost: 0
                Checking neighbor 8,7 of 8,8
                Adding state: 8,7 with total cost: 10.219544457292887
                Exploring state: 8,7, cost: 10.219544457292887
                Checking neighbor 8,6 of 8,7
                Adding state: 8,6 with total cost: 19.821869724335514
                Checking neighbor 8,8 of 8,7
                Exploring state: 8,6, cost: 19.821869724335514
                Checking neighbor 8,5 of 8,6
                Adding state: 8,5 with total cost: 28.884127472634063
                Checking neighbor 8,7 of 8,6
                Checking neighbor 7,6 of 8,6
                Adding state: 7,6 with total cost: 28.632119400242168
                Exploring state: 7,6, cost: 28.632119400242168
                Checking neighbor 6,6 of 7,6
                Adding state: 6,6 with total cost: 36.70318721210764
                Checking neighbor 8,6 of 7,6
                Exploring state: 8,5, cost: 28.884127472634063
                Checking neighbor 8,4 of 8,5
                Adding state: 8,4 with total cost: 37.49990057849797
                Checking neighbor 8,6 of 8,5
                Exploring state: 6,6, cost: 36.70318721210764
                Checking neighbor 6,5 of 6,6
                Adding state: 6,5 with total cost: 44.10631144954049
                Checking neighbor 7,6 of 6,6
                Checking neighbor 6,7 of 6,6
                Adding state: 6,7 with total cost: 45.5134368880143
                Exploring state: 8,4, cost: 37.49990057849797
                Checking neighbor 8,3 of 8,4
                Adding state: 8,3 with total cost: 45.78001046777849
                Checking neighbor 8,5 of 8,4
                Exploring state: 6,5, cost: 44.10631144954049
                Checking neighbor 5,5 of 6,5
                Adding state: 5,5 with total cost: 50.763165699032875
                Checking neighbor 6,6 of 6,5
                Exploring state: 6,7, cost: 45.5134368880143
                Checking neighbor 6,6 of 6,7
                Checking neighbor 6,8 of 6,7
                Adding state: 6,8 with total cost: 55.11576215505693
                Exploring state: 8,3, cost: 45.78001046777849
                Checking neighbor 8,4 of 8,3
                Exploring state: 5,5, cost: 50.763165699032875
                Checking neighbor 5,4 of 5,5
                Adding state: 5,4 with total cost: 56.763165699032875
                Checking neighbor 6,5 of 5,5
                Exploring state: 6,8, cost: 55.11576215505693
                Checking neighbor 6,7 of 6,8
                Checking neighbor 5,8 of 6,8
                Adding state: 5,8 with total cost: 64.17801990335548
                Exploring state: 5,4, cost: 56.763165699032875
                Checking neighbor 5,5 of 5,4
                Checking neighbor 5,3 of 5,4
                Adding state: 5,3 with total cost: 62.235301654032455
                Checking neighbor 4,4 of 5,4
                Adding state: 4,4 with total cost: 62.00580638615216
                Exploring state: 4,4, cost: 62.00580638615216
                Checking neighbor 3,4 of 4,4
                Adding state: 3,4 with total cost: 66.61135766161615
                Checking neighbor 5,4 of 4,4
                Exploring state: 5,3, cost: 62.235301654032455
                Checking neighbor 5,2 of 5,3
                Adding state: 5,2 with total cost: 67.35840727965011
                Checking neighbor 5,4 of 5,3
                Exploring state: 5,8, cost: 64.17801990335548
                Checking neighbor 4,8 of 5,8
                Adding state: 4,8 with total cost: 72.79379300921939
                Checking neighbor 6,8 of 5,8
                Exploring state: 3,4, cost: 66.61135766161615
                Checking neighbor 3,5 of 3,4
                Adding state: 3,5 with total cost: 72.08349361661573
                Checking neighbor 4,4 of 3,4
                Exploring state: 5,2, cost: 67.35840727965011
                Checking neighbor 5,1 of 5,2
                Adding state: 5,1 with total cost: 72.35840727965011
                Checking neighbor 5,3 of 5,2
                Exploring state: 3,5, cost: 72.08349361661573
                Checking neighbor 3,4 of 3,5
                Checking neighbor 3,6 of 3,5
                Adding state: 3,6 with total cost: 78.46865842375023
                Exploring state: 5,1, cost: 72.35840727965011
                Checking neighbor 6,1 of 5,1
                Adding state: 6,1 with total cost: 78.35840727965011
                Checking neighbor 5,2 of 5,1
                Exploring state: 4,8, cost: 72.79379300921939
                Checking neighbor 5,8 of 4,8
                Exploring state: 6,1, cost: 78.35840727965011
                Checking neighbor 5,1 of 6,1
                Exploring state: 3,6, cost: 78.46865842375023
                Checking neighbor 3,5 of 3,6
                Checking neighbor 3,7 of 3,6
                Adding state: 3,7 with total cost: 85.79321374408698
                Exploring state: 3,7, cost: 85.79321374408698
                Checking neighbor 3,6 of 3,7
                Checking neighbor 2,7 of 3,7
                Adding state: 2,7 with total cost: 92.87597627438521
                Exploring state: 2,7, cost: 92.87597627438521
                Checking neighbor 1,7 of 2,7
                Adding state: 1,7 with total cost: 99.87597627438521
                Checking neighbor 3,7 of 2,7
                Exploring state: 1,7, cost: 99.87597627438521
                Checking neighbor 1,6 of 1,7
                Adding state: 1,6 with total cost: 105.87597627438521
                Checking neighbor 2,7 of 1,7
                Exploring state: 1,6, cost: 105.87597627438521
                Checking neighbor 1,5 of 1,6
                Adding state: 1,5 with total cost: 110.87597627438521
                Checking neighbor 1,7 of 1,6
                Exploring state: 1,5, cost: 110.87597627438521
                Checking neighbor 1,4 of 1,5
                Adding state: 1,4 with total cost: 114.87597627438521
                Checking neighbor 1,6 of 1,5
                Exploring state: 1,4, cost: 114.87597627438521
                Checking neighbor 1,3 of 1,4
                Adding state: 1,3 with total cost: 117.87597627438521
                Checking neighbor 1,5 of 1,4
                Exploring state: 1,3, cost: 117.87597627438521
                Checking neighbor 1,2 of 1,3
                Adding state: 1,2 with total cost: 119.87597627438521
                Checking neighbor 1,4 of 1,3
                Exploring state: 1,2, cost: 119.87597627438521
                Checking neighbor 1,1 of 1,2
                Adding state: 1,1 with total cost: 120.87597627438521
                Checking neighbor 1,3 of 1,2
                Exploring state: 1,1, cost: 120.87597627438521
                Total states generated: 32
        '''
