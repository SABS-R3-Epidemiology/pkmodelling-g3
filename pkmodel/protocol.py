#
# Protocol class
#
import numpy as np

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    dose: numeric or list
        the amount of drug that enters the body
    T: list
        the time points when the drug is given
    dosing_pattern: str
        dosing protocol, either instanteneous or continuous
    dosing_type: str
        type of dosing, either intravenous or subcutaneous
    absorption_rate: numeric
        absorption rate for subcutaneous dosing. If dosing is intravenous, then k_a is 0
    """
    def __init__(self, dose, T, dosing_pattern, dosing_type, k_a = 0):
        self.dose, self.T, self.dosing_pattern, self.dosing_type = dose,T,dosing_pattern, dosing_type
        if self.dosing_type == 'subcutaneous':
            self.absorption_rate = k_a
        elif self.dosing_type == 'intravenous':
            self.absorption_rate = 0
        else:
            raise KeyError('Not correct dosing type')

    def dose_function(self):
        """ Construct the Dose(t) function for the PK model

        Create a function that models the dosing pattern, dosing time and dosing type

        """
        injection_function = []
        if self.dosing_pattern == 'instantaneous':
            sigma = 0.1
            for time in self.T:
                injection_function.append(np.exp(-np.power(t-time,2)/(2*np.power(sigma,2))))
        elif self.dosing_pattern == 'continuous':
            for time in self.T:
                injection_function.append()
            
        dose_function = sum(injection_function)

        if self.dosing_type == 'subcutaneous':
            subcutaneous_comp_function = lambda t: self.absorption_rate*q0
        elif self.dosing_type == 'intravenous':
            subcutaneous_comp_function = lambda t : dose_function

        return [dose_function,subcutaneous_comp_function]

