import unittest
import pkmodel as pk
import numpy as np


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_create(self):
        """
        Tests Solution creation.
        """
        
        with self.assertRaises(TypeError):
            test_model = 0
            test_protocol = pk.Protocol('subcutaneous','continuous',7,1000,T=[10])

        with self.assertRaises(TypeError):
            test_model = pk.Model(0, 1, [0], [0], 1)
            test_protocol = 0

    def test_solve(self):
        """
        Tests solve function
        """
         
        # Test the situation when Dose(t) is constant at 0, then the solution will remain at 0
        test_model = pk.Model(0, 1, [1], [0], 1)
        test_protocol = pk.Protocol('intravenous', 'continuous', 0)
        test_solution = solution(test_model, test_protocol, 10, 10)
        test_sol = test_solution.solve

        self.assertEqual(test_sol.y, np.zeros((3, 10)))
     
        # Test the situation when there is only the central compartment
        test_model = pk.Model(1, 1, [], [], 2)
        test_protocol = pk.Protocol('intravenous', 'continuous', 1)
        test_solution = Solution(test_model, test_protocol, 10, 10)
        test_sol = test_solution.solve

        self.assertEqual(test_sol.y, np.vstack((1 - np.exp(-test_sol.t), np.zeros((1, 10))))

        

