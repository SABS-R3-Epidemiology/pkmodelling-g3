import unittest
import pkmodel as pk


class ProtocolTest(unittest.TestCase):
    """
    Tests the :class:`Protocol` class.
    """
    def test_create(self):
        """
        Tests Protocol creation.
        """
        protocol = pk.Protocol('intravenous','instantaneous',[5],1000,T=[10])
        print(protocol())

if __name__ == '__main__':
    unittest.main()

protocol = Protocol('intravenous','instantaneous',[5],1000,T=[10])
print(protocol.create_subcutaneous_comp_function(10, 0.5))