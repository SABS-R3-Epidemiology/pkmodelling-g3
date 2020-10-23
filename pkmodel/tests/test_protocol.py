import unittest
import pkmodel as pk


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """

    def test_dose_function(self):
        """
        Tests dose function creation.
        """
        protocol = pk.Protocol('intravenous', 'instantaneous', [5],  T=[10])  # noqa
        self.assertAlmostEqual(protocol.create_dose_function(1), 0)

        protocol = pk.Protocol('subcutaneous', 'continuous', 7, T=[10])
        self.assertAlmostEqual(protocol.create_dose_function(4), 7)

    def test_subcutaneous_comp_function(self):
        """
        Tests subcutaneous compartment function creation.
        """
        protocol = pk.Protocol('intravenous', 'instantaneous', [5], T=[10])  # noqa
        self.assertAlmostEqual(protocol.create_subcutaneous_comp_function(0, 0.5), 0)  # noqa

        protocol = pk.Protocol('subcutaneous', 'continuous', 7, T=[10], absorption_rate=0.7)  # noqa
        self.assertAlmostEqual(protocol.create_subcutaneous_comp_function(0, 0.5), 0.35)  # noqa

    def test_errors(self):
        """
        Tests error raises
        """
        with self.assertRaises(TypeError):
            # check if error is raised when dose is not list
            # for instantaneous case
            pk.Protocol('subcutaneous','instantaneous',3)
        
        with self.assertRaises(TypeError):
            # check if error is raised when injection time is not list
            # for instantaneous case
            pk.Protocol('subcutaneous','instantaneous',[2],T=3)

        with self.assertRaises(ValueError):
            # check if error is raised when length of dose list is equal to length of injection time
            # for instantaneous case
            pk.Protocol('intravenous', 'instantaneous', [2, 5], T=[10])

        with self.assertRaises(TypeError):
            # check if error is raised when dose is not float or integer
            # for continuous case
            pk.Protocol('intravenous', 'continuous', [2])
        
        with self.assertRaises(KeyError):
            # check if error is raised when the dosing pattern is spelled wrongly
            pk.Protocol('subcutaneous', 'instataneous', [2])

        with self.assertRaises(KeyError):
            # check if error is raised when the dosing type is spelled wrongly
            pk.Protocol('intravanous', 'continuous', 2)
