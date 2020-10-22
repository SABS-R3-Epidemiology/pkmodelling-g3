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
        model1 = pk.Model(0, 1,[0],[0],1)
        self.assertEqual(model1.parameters, (0, 1,[0],[0],1))

        # Test wrong dimensions
        model2 = Model(0,0,[0,0],[0],1)
        self.assertRaises(model2, ValueError)

        model3 = Model(0,0,[0],[0],2)
        self.assertRaises(model3, ValueError)

        # Wrong type
        model4 = Model(0,[0,0],[0],[0],1)
        self.assertRaises(model4, TypeError)
        
        model5 = Model([0],0,[0],[0],1)
        self.assertRaises(model5, TypeError)

        model6 = Model(0,0,[0],[0],[1])
        self.assertRaises(model6, TypeError)

    def test_call(self):
        """
        Tests Model calling function.
        """
        model = pk.Model(0, 1,[0],[0],1)
        self.assertEqual(model, "new_model")

    def test_parameters(self):
        """
        Tests Model Parameter calling function.
        """
        model = pk.Model(0, 1,[0],[0],1)
        self.assertEqual(model.parameters, (0, 1,[0],[0],1))       
