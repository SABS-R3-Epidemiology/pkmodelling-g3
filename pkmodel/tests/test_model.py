import unittest
import pkmodel as pk


class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_create(self):
        """
        Tests Model creation.
        """
        # Creates a viable model
        model = pk.Model(0, 1, [0], [0], 1)
        self.assertEqual(model.parameters, (0, 1, [0], [0], 1))

        # Test wrong dimensions
        with self.assertRaises(ValueError):
            pk.Model(0, 0, [0, 0], [0], 1)

        with self.assertRaises(ValueError):
            pk.Model(0, 0, [0], [0], 2)

    def test_call(self):
        """
        Tests Model calling function.
        """
        model = pk.Model(0, 1, [0], [0], 1)
        self.assertEqual(str(model), "new_model")

    def test_parameters(self):
        """
        Tests Model Parameter calling function.
        """
        model = pk.Model(0, 1, [0], [0], 1)
        self.assertEqual(model.parameters, (0, 1, [0], [0], 1))
