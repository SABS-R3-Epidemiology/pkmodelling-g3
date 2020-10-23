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
            if type(dose) != float and type(dose) != int:
                raise TypeError('Not correct format for dose, please use float')

        else:
            raise KeyError('Not correct dosing pattern')

        if self.dosing_type == 'subcutaneous':
            self.absorption_rate = absorption_rate
        elif self.dosing_type == 'intravenous':
            self.absorption_rate = None
        else:
            raise KeyError('Not correct dosing type, either intravenous or subcutaneous')

    def create_dose_function(self, t):
        """ Creates a smooth step function

            Parameters
            ----------
            inject_time: numeric
                the time the drug is injected to the system
            height: numeric
                the amount of drug, which translates to the height of the function
            sharpness: numeric
                the steepness of the step function
            width: numeric
                the length of time when the drug is introducted

        """
        def bump_fn(t,inject_time,height,sharpness,width):
            """ Smooth step function for the dose function
            
            """
            return height / (1 + np.exp(sharpness*(t-inject_time))) - height / (1 + np.exp(sharpness*(t-inject_time+width)))

        sharpness = 30
        # Defines the steepness of the step function
        # Not defined by user

        dose_function = lambda t: 0
        if self.dosing_pattern == 'instantaneous':
        
            width = 0.1
            # Defines the width of the function
            # Not defined by user under the instantaneous case

            dose_function = lambda t: bump_fn(t,self.T[0],self.dose[0],sharpness,width)
            
            # for i in range(len(self.T)):
            #     d_f = lambda t: dose_function(t)
            #     print(d_f)
            #     dose_function = lambda t: bump_fn(t,self.T[i],self.dose[i],sharpness,width) + d_f(t)
        
        elif self.dosing_pattern == 'continuous':
        
            dose_function = lambda t: self.dose
        
            # for i in range(int(t_time/60)):
            #     d_f = lambda t: dose_function(t)
            #     dose_function = lambda t: bump_fn(t,i,self.dose,sharpness,self.dose_period) + d_f(t)

        return dose_function(t)
            

    def create_subcutaneous_comp_function(self, t, q):
        """ Construct the function for subcutaneous compartment of the PK model

        Create a function that models the way in which the drug is absorbed by the system.
        Uses absorption rate if dosing type is subcutaneous.

        """
        if self.dosing_type == 'subcutaneous':
            subcutaneous_comp_function = lambda t, q: self.absorption_rate*q
        elif self.dosing_type == 'intravenous':
            subcutaneous_comp_function = lambda t, q: self.create_dose_function(t)

        return subcutaneous_comp_function(t, q)
