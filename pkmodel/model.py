#
# Model class
# (Sets up main parameters and the number of peripheral
# compartments to be included in the model.)
#

class Model:
    """A Pharmokinetic (PK) model

    Parameter    Type   Description
    -----------  -----  --------------------------------------------------------------------------------------------
    name:        str    name of the model (optional)
    V_C:         float  volume of central compartment
    CL:          float  clearance/removal rate from central compartment
    num_periph:  int    number of peripheral compartments in the model
    V_P:         list   volumes of the peripheral compartments (length must be num_periph)
    Q_P:         list   transition rates between central and each peripheral compartment (length must be num_periph)
    -----------  -----  --------------------------------------------------------------------------------------------
    """
    def __init__(self, CL: float, V_C: float, V_P: list, Q_P: list, num_periph: int, name: str):
        """
        Create a model object
        """
        self.name = name
        self.V_C = V_C
        self.CL = CL

        self.num_periph = num_periph
        self.V_P = V_P
        self.Q_P = Q_P

        if len(V_P) != num_periph or len(Q_P) != num_periph:
            raise ValueError("V_P and Q_P must be vectors of length num_periph.")

    def __str__(self):
        """
        Call model object
        """
        return self.name
