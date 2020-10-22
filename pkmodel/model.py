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
    def __init__(self, CL: float, V_C: float, V_P: list, Q_P: list, num_periph: int, name: str = "new_model"):
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
    
    @property
    def parameters(self):
        """
        Call parameters of model in order:

        CL, V_c, V_p, Q_p, Number of peripheral compartments.
        """
        return self.CL, self.V_C, self.V_P, self.Q_P, self.num_periph


model1 = Model(0,0,[0],[0],1)
print(model1.parameters)
