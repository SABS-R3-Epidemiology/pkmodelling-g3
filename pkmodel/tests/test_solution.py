import unittest
import pkmodel as pk
import numpy as np
import numpy.testing as npt


class SolutionTest(unittest.TestCase):
    """
    Tests the :class:`Solution` class.
    """
    def test_create(self):
        """
        Tests Solution creation.
        """

        with self.assertRaises(TypeError):
            pk.Solution(0, pk.Protocol('subcutaneous', 'continuous', 7,T=[10]), 1000, 1)  # noqa

        with self.assertRaises(TypeError):
            pk.Solution(pk.Model(0, 1, [1], [0], 1), 0, 1000, 1)

    def test_solve(self):
        """
        Tests solve function
        """

        # Test the situation when Dose(t) is constant at 0, then the solution will remain at 0  # noqa
        test_model = pk.Model(0, 1, [1], [0], 1)
        test_protocol = pk.Protocol('intravenous', 'continuous', 0)
        test_solution = pk.Solution(test_model, test_protocol, 10, 10)
        test_sol = test_solution.solve

        npt.assert_array_almost_equal(test_sol.y, np.zeros((3, 10)), decimal=2)

        # Test the situation when there is only the central compartment
        test_model = pk.Model(1, 1, [], [], 0)
        test_protocol = pk.Protocol('intravenous', 'continuous', 1)
        test_solution = pk.Solution(test_model, test_protocol, 10, 10)
        test_sol = test_solution.solve

        npt.assert_array_almost_equal(test_sol.y, np.vstack((1 - np.exp(-test_sol.t), np.zeros((1, 10)))), decimal=2)  # noqa
