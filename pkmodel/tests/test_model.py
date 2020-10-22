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
        model = pk.Model()
        self.assertEqual(model.value, 42)


model1 = Model(0,0,[0],[0],1, "model1")
print(model1)

model2 = Model(0,0,[0,0],[0],1,"m2")
print(model2)

model3 = Model(0,0,[0],[0],2, "m3")
print(model3)

model4 = Model(0,[0,0],[0],[0],1, "m4")
print(model4)
