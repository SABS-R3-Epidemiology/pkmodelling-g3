import unittest
import pkmodel as pk


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """

    def test_dose_function(self):
        """
        Tests Protocol creation.
        """
        protocol = pk.Protocol('intravenous','instantaneous',[5],1000,T=[10])
        self.assertAlmostEqual(protocol.create_dose_function(1),0)

        protocol = pk.Protocol('subcutaneous','continuous',7,1000,T=[10])
        self.assertAlmostEqual(protocol.create_dose_function(4),7)

    def test_subcutaneous_comp_function(self):
        """
        Tests subcutaneous compartment function
        """
        protocol = pk.Protocol('intravenous','instantaneous',[5],1000,T=[10])
        self.assertAlmostEqual(protocol.create_subcutaneous_comp_function(0,0.5),0)

        protocol = pk.Protocol('subcutaneous','continuous',7,1000,T=[10],absorption_rate=0.7)
        self.assertAlmostEqual(protocol.create_subcutaneous_comp_function(0,0.5),0.35)

    def test_errors(self):
        """
        Tests error raises
        """

        with self.assertRaises(ValueError):
            pk.Protocol('intravenous','instantaneous',[2,5],1000,T=[10])

        with self.assertRaises(TypeError):
            pk.Protocol('intravenous','continuous',[2],1000)