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
    dose_period: numeric
        the time period for continuous dosing
        only for continuous dosing
    absorption_rate: numeric
        absorption rate for subcutaneous dosing. If dosing is intravenous, then not defined
    """
    def __init__(self, dosing_type, dosing_pattern, dose, t_time, T = None, dose_period = None, absorption_rate = None):
        self.dose, self.dosing_pattern, self.dosing_type, self.t_time = dose, dosing_pattern, dosing_type, t_time
        
        if self.dosing_pattern == 'instantaneous':
            self.T = T
            self.dose_period = None

            if type(dose) != list:
                raise TypeError('Not correct format for dose, please use list')
            if type(T) != list:
                raise TypeError('Not correct format for dosing times, please use list')
            if len(T) != len(dose):
                raise ValueError('Times and dose shots out of sync')
            

        elif self.dosing_pattern == 'continuous':
            self.T = None
            self.dose_period = dose_period
            if type(dose) != float:
                raise TypeError('Not correct format for dose, please use float')

        else:
            raise KeyError('Not correct dosing pattern')

        if self.dosing_type == 'subcutaneous':
            self.absorption_rate = absorption_rate
        elif self.dosing_type == 'intravenous':
            self.absorption_rate = None
        else:
            raise KeyError('Not correct dosing type, either intravenous or subcutaneous')

    def __call__(self):
        return [self.create_dose_function(),self.create_subcutaneous_comp_function()]

    def bump_fn(t,inject_time,height,sharpness,width):
        """ Smooth step function for the dose function
        
        """
        return height / [1 + np.exp(sharpness*(t-inject_time))] - height / [1 + np.exp(sharpness*(t-inject_time-width))]

    # @property
    def create_dose_function(self):
        """ Construct the Dose(t) function for the PK model

        Create a function that models the way in which the drug enters the system.
        Makes use of dosing pattern, dosing time and dosing type.

        """
        sharpness = 30
        # Defines the steepness of the step function

        self.dose_function = 0
        if self.dosing_pattern == 'instantaneous':
        
            width = 0.1
            # Defines

            for i in range(len(self.T)):
                self.dose_function += lambda t: self.bump_fn(t,self.T[i],self.dose[i],width,sharpness)
        elif self.dosing_pattern == 'continuous':
            for i in range(int(t_time/60)):
                self.dose_function += lambda t: self.bump_fn(t,i,self.dose,self.dose_period,sharpness)

        return self.dose_function
            

    # @property
    def create_subcutaneous_comp_function(self):
        """ Construct the Dose(t) function for the PK model

        Create a function that models the way in which the drug enters the system.
        Makes use of dosing pattern, dosing time and dosing type.

        """
        if self.dosing_type == 'subcutaneous':
            self.subcutaneous_comp_function = lambda t: self.absorption_rate*q0
        elif self.dosing_type == 'intravenous':
            self.subcutaneous_comp_function = self.dose_function

        return self.subcutaneous_comp_function

