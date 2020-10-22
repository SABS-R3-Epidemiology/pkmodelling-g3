#
# Protocol class
#
import numpy as np

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------
    dosing_type: str
        type of dosing, either intravenous or subcutaneous
    dosing_pattern: str
        dosing protocol, either instanteneous or continuous
    dose: numeric or list
        the amount of drug that enters the body
        numeric: for continuous dosing
        list: for instantaneous dosing
    T: list
        the time points when the drug is given
        only for instantaneous dosing
    absorption_rate: numeric
        absorption rate for subcutaneous dosing. If dosing is intravenous, then not defined
    """
    def __init__(self, dosing_type, dosing_pattern, dose, T = None, absorption_rate = None):
        self.dose, self.dosing_pattern, self.dosing_type = dose, dosing_pattern, dosing_type
        
        if self.dosing_pattern == 'instanteneous':
            self.T = T

            if len(T) != len(dose):
                raise ValueError('Times and dose shots out of sync')
            if type(dose) != list:
                raise TypeError('Not correct format for dose')
            if type(T) != list:
                raise TypeError('Not correct format for dosing times')

        elif self.dosing_pattern == 'continuous':
            self.T = None
            if type(dose) != float:
                raise TypeError('Not correct format for dose')

        else:
            raise KeyError('Not correct dosing pattern')

        if self.dosing_type == 'subcutaneous':
            self.absorption_rate = absorption_rate
        elif self.dosing_type == 'intravenous':
            self.absorption_rate = None
        else:
            raise KeyError('Not correct dosing type')

    @property
    def dose_function(self):
        """ Construct the Dose(t) function for the PK model

        Create a function that models the way in which the drug enters the system.
        Makes use of dosing pattern, dosing time and dosing type.

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

    @property
    def subcutaneous_comp_function(self):
        """ Construct the Dose(t) function for the PK model

        Create a function that models the way in which the drug enters the system.
        Makes use of dosing pattern, dosing time and dosing type.

        """
        if self.dosing_type == 'subcutaneous':
            subcutaneous_comp_function = lambda t: self.absorption_rate*q0
        elif self.dosing_type == 'intravenous':
            subcutaneous_comp_function = dose_function

        return [dose_function,subcutaneous_comp_function]

