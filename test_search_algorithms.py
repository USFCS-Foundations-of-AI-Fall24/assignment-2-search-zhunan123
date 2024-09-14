from unittest import TestCase
from mars_planner import *
from romania_state import *
from search_algorithms import *


class Test(TestCase):
    def test_breadth_first_search(self):
        def g(s):
            return s.loc == "battery"
        s = RoverState()
        result = breadth_first_search(s, action_list, g)
        print(result)
        def g2(s):
            return s.loc == "sample" and s.sample_extracted == True
        s2 = RoverState()
        result = breadth_first_search(s2, action_list, g2)
        print(result)
        def g3(s) :
            return s.charged == True and s.sample_extracted == True
        s3 = RoverState()
        result = breadth_first_search(s3, action_list, g3)
        print(result)

    def test_depth_first_search(self):
        def g(s):
            return s.loc == "battery"
        s = RoverState()
        result = depth_first_search(s, action_list, g)
        print(result)
        def g2(s):
            return s.loc == "sample" and s.sample_extracted == True
        s2 = RoverState()
        result = depth_first_search(s2, action_list, g2)
        print(result)
        def g3(s) :
            return s.charged == True and s.sample_extracted == True
        s3 = RoverState()
        result = depth_first_search(s3, action_list, g3)
        print(result)

    def test_depth_limited_search(self):
        def g(s):
            return s.loc == "battery"

        s = RoverState()
        result = depth_first_search(s, action_list, g, limit=2)
        print("Depth-limited search to battery (limit=2):", result)

        def g2(s):
            return s.loc == "sample" and s.sample_extracted == True

        s2 = RoverState()
        result = depth_first_search(s2, action_list, g2, limit=4)
        print("Depth-limited search to extract sample (limit=4):", result)

        def g3(s):
            return s.charged == True and s.sample_extracted == True

        s3 = RoverState()
        result = depth_first_search(s3, action_list, g3, limit=6)
        print("Depth-limited search to charge and extract sample (limit=6):", result)

    def test_decompose_problem(self):

        # Run the decompose problem function
        decompose_problem()
        print("\nDecomposition test completed.\n")

